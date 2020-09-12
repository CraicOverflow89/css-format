from css_format import CSSFormatter
import os, pytest


class TestCSSFormatter:
    def test_file_invalid(self) -> None:
        """
        Tests that invalid file paths throws FileNotFoundError
        :return: None
        """
        with pytest.raises(FileNotFoundError) as ex:
            CSSFormatter.format("/invalid/file.css")
        assert "No such file or directory" in str(ex)

    def test_file_valid(self) -> None:
        """
        Tests that no exception is thrown when file exists
        :return: None
        """
        test_file = "empty.css"
        initial_content = self._file_read(test_file)
        CSSFormatter.format(self._file_path(test_file))
        assert initial_content == self._file_read(test_file)

    def test_format_empty(self) -> None:
        """
        Tests that an empty content is handled without exception
        :return: None
        """
        CSSFormatter._format_str(self._file_read("empty.css"))

    def test_format_simple_spaces(self) -> None:
        """
        Tests that a simple file is formatted correctly with spaces
        :return: None
        """
        assert self._file_read("expect.css").replace(
            "\t", "    "
        ) == CSSFormatter._format_str(self._file_read("input.css"), indent_tabs=False)

    def test_format_simple_tabs(self) -> None:
        """
        Tests that a simple file is formatted correctly with tabs
        :return: None
        """
        assert self._file_read("expect.css") == CSSFormatter._format_str(
            self._file_read("input.css")
        )

    def _file_path(self, file: str) -> str:
        """
        Returns the absolute path of a file
        :param file: The test file to find the path of
        :return: string
        """
        return os.path.abspath(f"tests/resources/{file}")

    def _file_read(self, file: str) -> str:
        """
        Reads a test resource
        :param file: The test file to read
        :return: string
        """
        with open(f"tests/resources/{file}", "r") as fs:
            result = "\n".join(fs.read().splitlines())
        return result
