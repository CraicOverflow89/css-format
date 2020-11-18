import errno
import os


class CSSFormatter:
    @staticmethod
    def format(file: str) -> None:
        """
        Formats a css file
        :param file: Path to the file to format
        :return: None
        :raises FileNotFoundError: If file is invalid
        """
        if not os.path.exists(file) or not os.path.isfile(file):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file)
        with open(file, "r") as fs:
            result = CSSFormatter._format_str(fs.read())
        with open(file, "w") as fs:
            fs.write(result)

    @staticmethod
    def _format_str(value: str, indent_tabs: bool = True) -> str:
        """
        Formats a css string
        :param value: The css content to format
        :param indent_tabs: Indent with tabs instead of spaces
        :return: string
        """
        output = []
        indent = "\t" if indent_tabs else "    "
        in_block = False
        for line in value.splitlines():
            line = line.lstrip()
            if in_block:
                if line == "}":
                    in_block = False
                    output.append(line)
                else:
                    output.append(indent + line)
            else:
                if line.endswith("{"):
                    in_block = True
                output.append(line)
        return "\n".join(output)
