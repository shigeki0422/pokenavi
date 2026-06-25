"""
バトルログ記録
JSONL形式で /tmp/battle_log_YYYYMMDD.jsonl に保存
"""
import json
import time
from datetime import datetime
from pathlib import Path
from typing import Optional


class BattleRecorder:
    def __init__(self, log_dir: str = "/tmp"):
        today = datetime.now().strftime("%Y%m%d")
        self.path = Path(log_dir) / f"battle_log_{today}.jsonl"
        self._battle: dict = {}
        self._turns: list = []

    def start_battle(self, battle_id: int, my_team: list):
        self._battle = {
            "battle_id": battle_id,
            "start_time": time.time(),
            "my_team": my_team,
        }
        self._turns = []

    def record_turn(
        self,
        turn: int,
        state: str,
        move_names: list,
        chosen_idx: Optional[int],
        my_hp: float,
        opp_hp: float,
        opp_name: Optional[str] = None,
    ):
        self._turns.append({
            "turn": turn,
            "state": state,
            "move_names": move_names,
            "chosen_idx": chosen_idx,
            "chosen_move": move_names[chosen_idx] if chosen_idx is not None and move_names else None,
            "my_hp": round(my_hp, 3),
            "opp_hp": round(opp_hp, 3),
            "opp_name": opp_name,
            "ts": time.time(),
        })

    def end_battle(self, result: str):  # result: "win" | "lose" | "unknown"
        record = {
            **self._battle,
            "end_time": time.time(),
            "result": result,
            "turns": len(self._turns),
            "turn_log": self._turns,
        }
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
        print(f"[recorder] battle {self._battle.get('battle_id')} {result} — {self.path}")
        self._battle = {}
        self._turns = []
