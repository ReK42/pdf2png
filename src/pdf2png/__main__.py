"""CLI utility to convert PDF pages to PNG images."""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path
from typing import TYPE_CHECKING, Any

import click
from pypdf import PdfReader, PdfWriter
from rich.console import Console
from wand.color import Color
from wand.image import Image

from pdf2png import __copyright__, __name__, __version__  # noqa: A004

if TYPE_CHECKING:
    from collections.abc import Callable


_version: str = f"{__name__} v{__version__} -- {__copyright__}"


class IntRangeParamType(click.ParamType):
    """A parameter type for a list of integers."""

    name = "integer range"

    def convert(  # noqa: D102
        self,
        value: Any,  # noqa: ANN401
        param: click.Parameter | None,
        ctx: click.Context | None,
    ) -> list[int]:
        try:
            result: list[int] = []
            parts = value.split(",")
            for part in parts:
                if "-" in part:
                    first, last = part.split("-")
                    result.extend(range(int(first), int(last) + 1))
                else:
                    result.append(int(part))
        except (TypeError, ValueError):
            self.fail(f"{value!r} is not a valid page range", param, ctx)
        else:
            return result


@click.command()
@click.argument("file", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.option(
    "-p",
    "--pages",
    type=IntRangeParamType(),
    default=None,
    help="Pages to convert, will convert all if not specified. E.g.: 1,3-5,7",
)
@click.option("-r", "--resolution", type=int, default=None, help="Maximum dimension, in pixels")
@click.option("-d", "--dpi", type=int, default=300, help="DPI for converted image")
@click.option("-v", "--verbose", is_flag=True, help="Verbose output")
@click.help_option("-h", "--help")
@click.version_option(__version__, "--version", message=_version)
@click.pass_context
def main(  # noqa: PLR0913
    ctx: click.Context,
    file: Path = Path(),
    pages: list[int] | None = None,
    resolution: int | None = None,
    dpi: int = 300,
    verbose: bool = False,
) -> int:
    """
    CLI utility to convert PDF pages to PNG images.

    Run pdf2png COMMAND --help for details on each command.
    """
    ctx.ensure_object(dict)

    log_time_format: str = "[%Y-%m-%dT%H:%M:%S.%f%z]"
    get_datetime: Callable = lambda: datetime.now(timezone.utc).astimezone()  # noqa: E731
    ctx.obj["stdout"] = Console(
        log_time_format=log_time_format,
        get_datetime=get_datetime,
    )
    ctx.obj["stderr"] = Console(
        log_time_format=log_time_format,
        get_datetime=get_datetime,
        stderr=True,
    )

    stdout = ctx.obj["stdout"]
    stderr = ctx.obj["stderr"]  # noqa: F841

    if verbose and pages is None:
        stdout.print("Converting all pages...")
    elif verbose and pages is not None and len(pages) > 1:
        stdout.print(f"Converting pages {','.join(str(i) for i in pages)}...")

    stdout.print(f"Parsing {file}...")
    with PdfReader(file) as reader:
        if verbose:
            stdout.print(f"Found {len(reader.pages)} pages")
        if pages is None:
            pages = list(range(1, len(reader.pages) + 1))
        for page_num in pages:
            if verbose:
                stdout.print(f"Converting page {page_num}...")
            page = PdfWriter()
            page.add_page(reader.pages[page_num - 1])
            with BytesIO() as page_bytes:
                page.write(page_bytes)
                page_bytes.seek(0)
                with Image(file=page_bytes, resolution=dpi) as image:
                    if resolution is not None:
                        image.transform(resize=f"{resolution}x{resolution}>")
                    image.convert("png")
                    result = Image(width=image.width, height=image.height, background=Color("white"))
                    result.composite(image, operator="over")
                    result.save(filename=f"{file.stem} page {page_num:02d}.png")
                    stdout.print(f"Wrote page {page_num}...")

    return 1


if __name__ == "__main__":
    sys.exit(main(obj={}))
