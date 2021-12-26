from pytest import fixture

from convert_buffer import ConvertBuffer


@fixture
def convert_buffer() -> ConvertBuffer:
    return ConvertBuffer()


class TestBufferConverter:
    def test_conversion_to_str(self, convert_buffer):
        buffer = ['first', 'second']

        str_content = convert_buffer.convert_buffer_to_str(buffer)

        assert str_content == 'first\nsecond'
