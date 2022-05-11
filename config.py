from dataclasses import dataclass

@dataclass
class RipConfiguration:
  """Class for keeping track of the configuration of the PDF ripper settings"""
  _n_pages: int
  _start_page: int
  _end_page: int
  _topLeftCoords: tuple = (0, 0)
  _bottomRightCoords: tuple = (0, 0)
  (_page_selection_box_X, _page_selection_box_Y) = (0, 0)
  _should_coords_be_doubled_bool: bool = False

  @property
  def n_pages(self) -> int:
    return self._n_pages

  @n_pages.setter
  def n_pages(self, n_pages: int) -> None:
    self._n_pages = n_pages

  @property
  def start_page(self) -> int:
    return self._start_page
  
  @start_page.setter
  def start_page(self, start_page: int) -> None:
    self._start_page = start_page

  @property
  def end_page(self) -> int:
    return self._end_page

  @end_page.setter
  def end_page(self, end_page: int) -> None:
    self._end_page = end_page
  
  @property
  def topLeftCoords(self) -> int:
    return self._topLeftCoords

  @topLeftCoords.setter
  def topLeftCoords(self, topLeftCoords: int) -> None:
    self._topLeftCoords = topLeftCoords

  @property
  def bottomRightCoords(self) -> tuple:
    return self._bottomRightCoords

  @bottomRightCoords.setter
  def bottomRightCoords(self, bottomRightCoords: tuple) -> None:
    self._bottomRightCoords = bottomRightCoords

  @property
  def page_selection_box_X(self) -> int:
    return self._page_selection_box_X

  @page_selection_box_X.setter
  def page_selection_box_X(self, page_selection_box_X: int) -> None:
    self._page_selection_box_X = page_selection_box_X

  @property
  def page_selection_box_Y(self) -> int:
    return self._page_selection_box_Y

  @page_selection_box_Y.setter
  def page_selection_box_Y(self, page_selection_box_Y: int) -> None:
    self._page_selection_box_Y = page_selection_box_Y
  
  @property
  def should_coords_be_doubled_bool(self) -> bool:
    return self._should_coords_be_doubled_bool

  @should_coords_be_doubled_bool.setter
  def should_coords_be_doubled_bool(self, should_coords_be_doubled_bool: bool) -> None:
    self._should_coords_be_doubled_bool = should_coords_be_doubled_bool