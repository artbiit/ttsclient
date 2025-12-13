from pathlib import Path
from typing import Literal, TypeAlias
import sys

# GLOBAL CONSTANTS
HERE = Path(__file__).parent.absolute()


def get_version():
    with open(HERE / "version.txt", "r", encoding="utf-8") as f:
        return f.read().strip()


APP_NAME = "TTSClient"
VERSION = get_version()
LOGGER_NAME = "ttsclient"
LOG_FILE = Path("ttsclient.log")
ModuleDir = Path("modules")

UPLOAD_DIR_STR = "upload_dir"
# UPLOAD_DIR = Path(UPLOAD_DIR_STR)
UPLOAD_DIR = HERE.parent / UPLOAD_DIR_STR
UPLOAD_DIR.mkdir(exist_ok=True)

SSL_KEY_DIR = Path("ssl_key")


def get_frontend_path():
    frontend_path = "web_front"
    return Path(frontend_path)


# Client
NATIVE_CLIENT_FILE_WIN = Path(sys._MEIPASS, "native_client", "voice-changer-native-client.exe") if hasattr(sys, "_MEIPASS") else Path("native_client", "voice-changer-native-client.exe")
NATIVE_CLIENT_FILE_MAC = Path(
    "voice-changer-native-client.app",
    "Contents",
    "MacOS",
    "voice-changer-native-client",
)


# TTS モジュール
TTSType: TypeAlias = Literal["GPT-SoVITS", "BROKEN", "RESERVED_FOR_SAMPLE", "VoiceCharacter"]
TTSTypes: list[TTSType] = [
    "GPT-SoVITS",
    "BROKEN",
    "RESERVED_FOR_SAMPLE",
    "VoiceCharacter",
]

GPTSoVITSVersion: TypeAlias = Literal["v1", "v2"]
GPTSoVITSVersions: list[GPTSoVITSVersion] = [
    "v1",
    "v2",
]

GPTSoVITSModelVersion: TypeAlias = Literal["v1", "v2", "v3", "v4"]
GPTSoVITSModelVersions: list[GPTSoVITSVersion] = [
    "v1",
    "v2",
    "v3",
    "v4",
]

SemanticPredictorType: TypeAlias = Literal["GPTSemanticPredictor",]
SemanticPredictorTypes: list[SemanticPredictorType] = [
    "GPTSemanticPredictor",
]

PhoneExtractorType: TypeAlias = Literal["BertPhoneExtractor",]
PhoneExtractorTypes: list[PhoneExtractorType] = [
    "BertPhoneExtractor",
]

SynthesizerType: TypeAlias = Literal["SovitsSynthesizer", "SovitsSynthesizerV3", "SovitsSynthesizerV3Lora", "SovitsSynthesizerV4", "SovitsSynthesizerV4Lora"]
SynthesizerTypes: list[SynthesizerType] = [
    "SovitsSynthesizer",
    "SovitsSynthesizerV3",
    "SovitsSynthesizerV3Lora",
    "SovitsSynthesizerV4",
    "SovitsSynthesizerV4Lora",
]

EmbedderType: TypeAlias = Literal["cnhubert",]
EmbedderTypes: list[EmbedderType] = [
    "cnhubert",
]

# Configu Manager
SettingsDir = Path("./settings")
SettingsDir.mkdir(parents=True, exist_ok=True)
ConfigFile = SettingsDir / "tts_conf.json"

# Slot Manager
ModelDir = Path("./models")
ModelDir.mkdir(parents=True, exist_ok=True)
MAX_SLOT_INDEX = 20
SLOT_PARAM_FILE = "params.json"
GPT_SOVITS_USER_DICT_PATH = Path(sys._MEIPASS, "third_party", "GPT-SoVITS", "GPT_SoVITS", "text", "ja_userdic", "userdict.csv") if hasattr(sys, "_MEIPASS") else Path("third_party", "GPT-SoVITS", "GPT_SoVITS", "text", "ja_userdic", "userdict.csv")
OPENJTALK_USER_DICT_CSV_FILE = "user_dict.csv"
OPENJTALK_USER_DICT_TEMP_CSV_FILE = "user_dict_tmp.csv"
OPENJTALK_USER_DICT_FILE = "user_dict.dict"


# Voice Character Slot Manager
VoiceCharacterDir = Path("./voice_characters")
VoiceCharacterDir.mkdir(parents=True, exist_ok=True)
MAX_VOICE_CHARACTER_SLOT_INDEX = 200
VOICE_CHARACTER_SLOT_PARAM_FILE = "params.json"
MAX_REFERENCE_VOICE_SLOT_INDEX = 100

# BasicVoiceType: TypeAlias = Literal["anger", "disgust", "fear", "happy", "sad", "surprise"]
# BasicVoiceTypes: list[BasicVoiceType] = [
#     "anger",
#     "disgust",
#     "fear",
#     "happy",
#     "sad",
#     "surprise",
# ]

LanguageType: TypeAlias = Literal[
    "all_zh",  # 全部按中文识别
    "en",  # 全部按英文识别#######不变
    "all_ja",  # 全部按日文识别
    "all_yue",  # 全部按中文识别
    "all_ko",  # 全部按韩文识别
    "zh",  # 按中英混合识别####不变
    "ja",  # 按日英混合识别####不变
    "yue",  # 按粤英混合识别####不变
    "ko",  # 按韩英混合识别####不变
    "auto",  # 多语种启动切分识别语种
    "auto_yue",  # 多语种启动切分识别语种
]
LanguageTypes: list[LanguageType] = [
    "all_zh",
    "en",
    "all_ja",
    "all_yue",
    "all_ko",
    "zh",
    "ja",
    "yue",
    "ko",
    "auto",
    "auto_yue",
]

CutMethod: TypeAlias = Literal[
    "No slice",
    "Slice once every 4 sentences",
    "Slice per 50 characters",
    "Slice by Chinese punct",
    "Slice by English punct",
    "Slice by every punct",
]
CutMethods: list[CutMethod] = [
    "No slice",
    "Slice once every 4 sentences",
    "Slice per 50 characters",
    "Slice by Chinese punct",
    "Slice by English punct",
    "Slice by every punct",
]

CutMethodForFaster: TypeAlias = Literal[
    "cut0",
    "cut1",
    "cut2",
    "cut3",
    "cut4",
    "cut5",
]
CutMethodsForFaster: list[CutMethodForFaster] = [
    "cut0",
    "cut1",
    "cut2",
    "cut3",
    "cut4",
    "cut5",
]

BackendMode: TypeAlias = Literal[
    "all_torch",
    "all_onnx",
    "semantic_onnx",
    "synthesizer_onnx",
]

TranscriberModelSize: TypeAlias = Literal[
    "tiny",
    "base",
    "small",
    "medium",
    "large-v1",
    "large-v2",
    "large-v3",
    "large",
    "distil-large-v2",
    "distil-large-v3",
    "large-v3-turbo",
    "turbo",
]
TranscriberModelSizes: list[TranscriberModelSize] = [
    "tiny",
    "base",
    "small",
    "medium",
    "large-v1",
    "large-v2",
    "large-v3",
    "large",
    "distil-large-v2",
    "distil-large-v3",
    "large-v3-turbo",
    "turbo",
]

TranscriberDevice: TypeAlias = Literal[
    "cpu",
    "cuda",
]
TranscriberDevices: list[TranscriberDevice] = [
    "cpu",
    "cuda",
]

TranscriberComputeType: TypeAlias = Literal[
    "int8",
    "int8_float32",
    "int8_float16",
    "int8_bfloat16",
    "int16",
    "float16",
    "bfloat16",
    "float32",
]
TranscriberComputeTypes: list[TranscriberComputeType] = [
    "int8",
    "int8_float32",
    "int8_float16",
    "int8_bfloat16",
    "int16",
    "float16",
    "bfloat16",
    "float32",
]
