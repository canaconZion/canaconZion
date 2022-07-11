import websockets
import asyncio
import utils
import json


class ScoutJanus:
    def __init__(self, server, room, target_display):
        self.server = server
        self.room = room
        self.target_dispaly = target_display
        self.result = False

    def scout(self):
        loop = asyncio.get_event_loop()

        loop.run_until_complete(self._do_scout())

    async def _do_scout(self):
        self.conn = await websockets.connect(self.server, subprotocols=['janus-protocol'])
        transaction = utils.guid()
        await self.conn.send(json.dumps({
            "janus": "create",
            "transaction": transaction
        }))
        resp = json.loads(await self.conn.recv())
        session = resp["data"]["id"]

        transaction = utils.guid()
        await self.conn.send(json.dumps({
            "janus": "attach",
            "session_id": session,
            "plugin": "janus.plugin.videoroom",
            "transaction":  transaction
        }))
        resp = json.loads(await self.conn.recv())
        handle = resp['data']['id']

        transaction = utils.guid()
        await self.conn.send(json.dumps({
            "janus": "message",
            "body": {
                "request": "listparticipants",
                "room": self.room
            },
            "transaction": transaction,
            "session_id": session,
            "handle_id": handle
        }))
        resp = json.loads(await self.conn.recv())

        try:
            for p in resp['plugindata']['data']['participants']:
                if p['display'] == self.target_dispaly:
                    self.result = True
                    break
        except:
            pass


if __name__ == '__main__':
    js = ScoutJanus("ws://dev.smt.dyinnovations.com:8188", 'stationary-m210test', "stationary-m210test_JIWEI")
    js.scout()
    print(js.result)