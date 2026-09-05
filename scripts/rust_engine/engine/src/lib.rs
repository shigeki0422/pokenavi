//! ポケナビ対戦エンジンの Rust レプリカ（Pythonが仕様の正本）。
//! R0: データパック・spec解析・ステータス計算 / R1: calc_damage
#![allow(uncommon_codepoints, mixed_script_confusables, non_snake_case)]
pub mod abilities;
pub mod ai;
pub mod analysis;
pub mod battle;
pub mod belief;
pub mod cpyrng;
pub mod damage;
pub mod features;
pub mod net;
pub mod search;
pub mod items;
pub mod live;
pub mod oppview;
pub mod rng;
pub mod sim;
pub mod statec;
pub mod interner;
pub mod pack;
pub mod poke;
pub mod pysum;
pub mod syms;

pub use pack::Pack;
