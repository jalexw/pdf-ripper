from dataclasses import dataclass

@dataclass(frozen=True)
class RipConfiguration:
  """Class for keeping track of the configuration of the PDF ripper settings"""
  start_page: int
  end_page: int
  topLeftCoords: tuple[float, float]
  bottomRightCoords: tuple[float, float]
  pageSelectionCoords: tuple[float, float]
  doubleCoords: bool
  outputDir: str
  screenshotDelay: float
