class BookNotFoundError(Exception):
    """unnamed header exception"""
    def __init__(self) -> None:
        super().__init__("Book not found.")
