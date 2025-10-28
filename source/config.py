from pyrogram import Client,filters,enums
import redis
r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    charset="utf-8",
    decode_responses=True
    )

sudo_id = 6848908141
bot_user = "physical2bot"
api_id = 17104807
api_hash = "082b437fa75ed409a45b8660b95a97c0"
session = "1ApWapzMBuxm-jGRxmnAMG3pnOQFgHn3AJIDmGwODOaAZR8Sg-_SnugSjH6YDK1Iv-hh_e2xywHQOTOYKGWsWaWNMirr6FH-9CH-XpZjcr_cDZtLsze8Fv78UtzWTECrlX0BaBlw_UgchPmh_1rTWL2IsHj0haprF2ax0HPzD6cpTC61Ks8jYzlUFWC1X0pQjIUd2JubulJ83_gxpT4vVznO5MUsykd-RfKEVV0bmo3SSyMm5wNkScPQl8VG9JPlN4uMKVvyg-g1qdvl0IsFaW7NDHTCKcEiQZG78HFGbv1k8yWj4gCM33EOB-_dk9s7TiW7O-6mZWnBEjs1c2EN-UfzzLBYoL9c="
token = "7665348559:AAE-gaBCPLAkKV5s7BQPIQmZUxoOgaaBAGA"
sudo_command = [6848908141]
pm = "-1002718737593"
mention = "-1002718737593"
plugins = dict(root="plugins")
app = Client("user:Amrsabrrybot",api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)
bot = Client("Amrsabrrybot",api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))
