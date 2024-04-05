"""
Functions and routines associated with Enasis Network Common Library.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from pathlib import Path

from _pytest.logging import LogCaptureFixture

from pytest import fixture

from ..logger import Logger
from ..logger import Message
from ...times.common import UNIXMPOCH
from ...utils.stdout import strip_ansi



@fixture
def logger(
    tmp_path: Path,
) -> Logger:
    """
    Construct the instance for use in the downstream tests.

    :param tmp_path: pytest object for temporal filesystem.
    :returns: Newly constructed instance of related class.
    """

    path = f'{tmp_path}/test.log'

    return Logger(
        stdo_level='info',
        file_level='info',
        file_path=path)



def test_Message() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    message = Message(
        time=UNIXMPOCH,
        level='info',
        dict={'foo': 'bar'},
        empty=[],
        float=1.0,
        int=1,
        list=[1, '2', 3],
        none=None,
        string='foo',
        elapsed=0.69420)


    attrs = list(message.__dict__)

    assert attrs == [
        '_Message__level',
        '_Message__time',
        '_Message__fields']


    assert repr(message)[:26] == (
        'Message(level="info", time')

    assert hash(message) > 0

    assert str(message)[:26] == (
        'Message(level="info", time')


    assert message.level == 'info'
    assert message.time == '1970-01-01'
    assert message.fields == {
        'dict': "{'foo': 'bar'}",
        'float': '1.0',
        'int': '1',
        'list': "[1, '2', 3]",
        'string': 'foo',
        'elapsed': '0.69'}


    assert repr(message) == (
        'Message('
        'level="info", '
        f'time="{UNIXMPOCH}", '
        'dict="{\'foo\': \'bar\'}", '
        'float="1.0", '
        'int="1", '
        'list="[1, \'2\', 3]", '
        'string="foo", '
        'elapsed="0.69")')


    output = strip_ansi(
        message.stdo_output)

    assert output == (
        'level="info"'
        ' time="1970-01-01T00:00:00Z"'
        ' dict="{\'foo\': \'bar\'}"'
        ' float="1.0"'
        ' int="1"'
        ' list="[1, \'2\', 3]"'
        ' string="foo"'
        ' elapsed="0.69"')


    assert message.file_output == (
        '{"level": "info",'
        f' "time": "{UNIXMPOCH}",'
        ' "dict": "{\'foo\': \'bar\'}",'
        ' "float": "1.0",'
        ' "int": "1",'
        ' "list": "[1, \'2\', 3]",'
        ' "string": "foo",'
        ' "elapsed": "0.69"}')



def test_Logger(
    logger: Logger,
    caplog: LogCaptureFixture,
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param logger: Custom fixture for the logger instance.
    :param caplog: pytest object for capturing log message.
    """


    attrs = list(logger.__dict__)

    assert attrs == [
        '_Logger__stdo_level',
        '_Logger__file_level',
        '_Logger__file_path',
        '_Logger__started',
        '_Logger__logger_stdo',
        '_Logger__logger_file']


    assert repr(logger)[:23] == (
        '<encommon.config.logger')

    assert hash(logger) > 0

    assert str(logger)[:23] == (
        '<encommon.config.logger')


    assert logger.stdo_level == 'info'
    assert logger.file_level == 'info'
    assert logger.file_path is not None
    assert logger.started is False
    assert logger.logger_stdo is not None
    assert logger.logger_file is not None

    logger.log_d(msg='pytest')
    logger.log_c(msg='pytest')
    logger.log_e(msg='pytest')
    logger.log_i(msg='pytest')
    logger.log_w(msg='pytest')



def test_Logger_cover(
    logger: Logger,
    caplog: LogCaptureFixture,
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param logger: Custom fixture for the logger instance.
    :param caplog: pytest object for capturing log message.
    """


    def _logger_logs() -> None:
        logger.log_d(msg='pytest')
        logger.log_c(msg='pytest')
        logger.log_e(msg='pytest')
        logger.log_i(msg='pytest')
        logger.log_w(msg='pytest')


    _caplog = list[tuple[str, int, str]]


    def _logger_stdo() -> _caplog:

        output = caplog.record_tuples
        key = 'encommon.logger.stdo'

        return [
            x for x in output
            if x[0] == key]


    def _logger_file() -> _caplog:

        output = caplog.record_tuples
        key = 'encommon.logger.file'

        return [
            x for x in output
            if x[0] == key]


    logger.start()

    _logger_logs()

    assert len(_logger_stdo()) == 5
    assert len(_logger_file()) == 5

    logger.stop()


    _logger_logs()

    assert len(_logger_stdo()) == 5
    assert len(_logger_file()) == 5


    logger.start()

    message = 'unknown exception'
    raises = Exception('pytest')

    logger.log_e(
        message=message,
        exc_info=raises)

    stdo = _logger_stdo()[-1][2]
    file = _logger_file()[-1][2]

    assert message in str(stdo)
    assert message in str(file)

    assert len(_logger_stdo()) == 6
    assert len(_logger_file()) == 6

    logger.stop()


    _logger_logs()

    assert len(_logger_stdo()) == 6
    assert len(_logger_file()) == 6
