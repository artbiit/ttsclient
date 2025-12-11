import io
from typing import Optional
import wave
from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from ttsclient.const import LanguageType
from ttsclient.server.validation_error_logging_route import ValidationErrorLoggingRoute
from ttsclient.tts.data_types.tts_manager_data_types import GenerateVoiceParam, GetPhonesParam, GetPhonesResponse, GetJpTextToUserDictRecordsParam
from ttsclient.tts.tts_manager.tts_manager import TTSManager

# import soundfile as sf


# YMM4 向けhack
class MoraTone(BaseModel):
    mora: str
    tone: int


class SynthesisParam(BaseModel):
    model: str
    modelFile: str
    text: str
    moraToneList: list[MoraTone]
    style: str
    styleWeight: float = 0
    assistText: str = ""
    assistTextWeight: float = 0
    speed: float = 1.0
    noise: float = 0
    noisew: float = 0
    sdpRatio: float = 0
    language: str = "auto"
    silenceAfter: float = 0
    pitchScale: float = 0
    intonationScale: float = 0
    speaker: Optional[str] = None


class G2PParam(BaseModel):
    text: str


class RestAPITTSManager:
    def __init__(self):
        self.router = APIRouter()
        self.router.route_class = ValidationErrorLoggingRoute

        self.router.add_api_route("/api/tts-manager/operation/generateVoice", self.post_generate_voice, methods=["POST"])
        self.router.add_api_route("/api/tts-manager/operation/getPhones", self.post_get_phones, methods=["POST"])
        self.router.add_api_route("/api/tts-manager/operation/getJpTextToUserDictRecords", self.post_jp_text_to_user_dict_records, methods=["POST"])

        self.router.add_api_route("/api_tts-manager_operation_generateVoice", self.post_generate_voice, methods=["POST"])
        self.router.add_api_route("/api_tts-manager_operation_getPhones", self.post_get_phones, methods=["POST"])
        self.router.add_api_route("/api_tts-manager_operation_getJpTextToUserDictRecords", self.post_jp_text_to_user_dict_records, methods=["POST"])

        # YMM4 向けhack
        self.router.add_api_route("/api/g2p", self.post_g2p_ymm4, methods=["POST"])
        self.router.add_api_route("/api/synthesis", self.post_synthesis_ymm4, methods=["POST"])

    def post_get_phones(self, get_phones_param: GetPhonesParam):
        phones, phone_symboles = TTSManager.get_instance().get_phones(get_phones_param)
        res = GetPhonesResponse(phones=phones, phone_symbols=phone_symboles)
        return res

    def post_jp_text_to_user_dict_records(self, get_jp_text_to_user_dict_records_param: GetJpTextToUserDictRecordsParam):
        records = TTSManager.get_instance().jp_text_to_user_dict_records(get_jp_text_to_user_dict_records_param)
        return records

    def post_generate_voice(self, generarte_voice_param: GenerateVoiceParam, request: Request):
        last_sampling_rate, last_audio_data = TTSManager.get_instance().run(generarte_voice_param)
        # sf.write("output.wav", last_audio_data, last_sampling_rate)

        audio_buffer = io.BytesIO()
        with wave.open(audio_buffer, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)  # 2 bytes for 16-bit audio
            wf.setframerate(last_sampling_rate)
            wf.writeframes(last_audio_data.tobytes())

        audio_buffer.seek(0)

        return StreamingResponse(audio_buffer, media_type="audio/wav", headers={
            "Content-Disposition": 'inline; filename="output.wav"',
            "Access-Control-Expose-Headers": "Content-Disposition"
        })

        # with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        #     tmp_file_name = tmp_file.name
        #     with wave.open(tmp_file_name, "w") as wf:
        #         wf.setnchannels(1)
        #         wf.setsampwidth(2)  # 2 bytes for 16-bit audio
        #         wf.setframerate(last_sampling_rate)
        #         wf.writeframes(last_audio_data.tobytes())

        # try:
        #     return FileResponse(tmp_file_name, media_type="audio/wav", filename="output.wav")
        # finally:
        #     os.remove(tmp_file_name)

    def post_synthesis_ymm4(self, param: SynthesisParam):
        print(param)

        voice_character_slot_index = int(param.speaker.split("_")[0])
        reference_voice_slot_index = int(param.style.split("_")[0])

        dummy_param = GenerateVoiceParam(
            voice_character_slot_index=voice_character_slot_index,
            reference_voice_slot_index=reference_voice_slot_index,
            text=param.text,
            language="auto",
            # language="all_ja",
            # language="auto_yue",
            speed=1,
            cutMethod="No slice",
            sample_steps=16,
        )
        return self.post_generate_voice(dummy_param)

    def post_g2p_ymm4(self, param: G2PParam):
        dummy: list[MoraTone] = [
            MoraTone(mora="ダ", tone=0),
            MoraTone(mora="ミ", tone=0),
            MoraTone(mora="イ", tone=0),
        ]
        return dummy
