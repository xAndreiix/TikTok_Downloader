import os
import pytest
import requests
from unittest.mock import patch, MagicMock
import main


@patch("builtins.input", return_value="https://www.tiktok.com/@test/video/123")
@patch("requests.get")
def test_download_tiktok_video_without_watermark(mock_get, mock_input, tmp_path):
    mock_response_api = MagicMock()
    mock_response_api.json.return_value = {
        "data": {
            "play": "http://example.com/fakevideo.mp4"
        }
    }
    mock_response_api.status_code = 200
    mock_get.side_effect = [mock_response_api, MagicMock(content=b"fake video data")]

    os.chdir(tmp_path)

    main.download_tiktok_video_without_watermark()

    output_file = tmp_path / "tiktok_video_without_watermark.mp4"
    assert output_file.exists()
    assert output_file.read_bytes() == b"fake video data"
