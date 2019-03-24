from header_music import *
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

# WARNING: You MUST add mtf_module_track flag to the flags of the tracks located under module directory

tracks = [
##  ("losing_battle", "alosingbattle.mp3", sit_calm|sit_action),
##  ("reluctant_hero", "reluctanthero.mp3", sit_action),
##  ("the_great_hall", "thegreathall.mp3", sit_calm),
##  ("requiem", "requiem.mp3", sit_calm),
##  ("silent_intruder", "silentintruder.mp3", sit_calm|sit_action),
##  ("the_pilgrimage", "thepilgrimage.mp3", sit_calm),
##  ("ambushed", "ambushed.mp3", sit_action),
##  ("triumph", "triumph.mp3", sit_action),

##  ("losing_battle", "alosingbattle.mp3", mtf_sit_map_travel|mtf_sit_attack),
##  ("reluctant_hero", "reluctanthero.mp3", mtf_sit_attack),
##  ("the_great_hall", "thegreathall.mp3", mtf_sit_map_travel),
##  ("requiem", "requiem.mp3", mtf_sit_map_travel),
##  ("silent_intruder", "silentintruder.mp3", mtf_sit_map_travel|mtf_sit_attack),
##  ("the_pilgrimage", "thepilgrimage.mp3", mtf_sit_map_travel),
##  ("ambushed", "ambushed.mp3", mtf_sit_attack),
##  ("triumph", "triumph.mp3", mtf_sit_attack),
  ("bogus", "cant_find_this.ogg", 0, 0),
  ("mount_and_blade_title_screen", "mount_and_blade_title_screen.ogg", mtf_module_track|mtf_sit_main_title|mtf_start_immediately, 0),

  ("ambushed_by_neutral", "nanman.ogg", mtf_module_track|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight),
  ("ambushed_by_khergit", "fight_as_hebei.ogg", mtf_module_track|mtf_culture_3|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  ("ambushed_by_nord",    "fight_two.ogg", mtf_module_track|mtf_culture_4|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  ("ambushed_by_rhodok",  "fight_as_wu.ogg", mtf_module_track|mtf_culture_5|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  ("ambushed_by_swadian", "frght_as_wei.ogg", mtf_module_track|mtf_culture_1|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  ("ambushed_by_vaegir",  "fight_as_shu.ogg", mtf_module_track|mtf_culture_2|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  ("ambushed_by_sarranid", "fight_one.ogg", mtf_module_track|mtf_culture_6|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_culture_all),
  
  ("arena_1", "lvbu.ogg", mtf_module_track|mtf_sit_arena, 0),
#  ("arena_2", "arena_2.ogg", mtf_looping|mtf_sit_arena, 0),
  ("armorer", "lvxing_1.ogg", mtf_module_track|mtf_sit_travel, 0),
  ("bandit_fight", "fight_one.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),

  ("calm_night_1", "yiyeshu.ogg", mtf_module_track|mtf_sit_night, mtf_sit_town|mtf_sit_tavern|mtf_sit_travel),
  ("captured", "gongting.ogg", mtf_module_track|mtf_persist_until_finished, 0),
  ("defeated_by_neutral", "shu1.ogg",mtf_module_track|mtf_persist_until_finished|mtf_sit_killed, 0),
  ("defeated_by_neutral_2", "shu2.ogg", mtf_module_track|mtf_persist_until_finished|mtf_sit_killed, 0),
  ("defeated_by_neutral_3", "suzhan2.ogg", mtf_module_track|mtf_persist_until_finished|mtf_sit_killed, 0),

  ("empty_village", "wolongyin.ogg", mtf_module_track|mtf_persist_until_finished, 0),
  ("encounter_hostile_nords", "gongting.ogg", mtf_module_track|mtf_persist_until_finished|mtf_sit_encounter_hostile, 0),
  ("escape", "escape.ogg", mtf_module_track|mtf_persist_until_finished, 0),

  ("fight_1", "fight_one.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  ("fight_2", "fight_two.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  ("fight_3", "fight_as_wu.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  ("fight_as_khergit", "fight_as_hebei.ogg", mtf_module_track|mtf_culture_3|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, mtf_culture_all),
  ("fight_4", "nanman.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),  
  ("fight_as_nord", "fight_as_wu.ogg", mtf_module_track|mtf_culture_4|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, mtf_culture_all),
  ("fight_as_rhodok", "frght_as_wei.ogg", mtf_module_track|mtf_culture_5|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, mtf_culture_all),
#  ("fight_as_swadian", "fight_as_swadian.ogg", mtf_culture_1|mtf_sit_fight|mtf_sit_multiplayer_fight, mtf_culture_all),
  ("fight_as_vaegir", "fight_as_shu.ogg", mtf_module_track|mtf_culture_2|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, mtf_culture_all),
  ("fight_while_mounted_1", "gongcheng.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  ("fight_while_mounted_2", "fight_as_shu.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  ("fight_while_mounted_3", "frght_as_wei.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  
  ("infiltration_khergit", "yiyeshu.ogg", mtf_module_track|mtf_culture_3|mtf_sit_town_infiltrate, mtf_culture_all),

  ("killed_by_khergit", "wushuang1.ogg", mtf_module_track|mtf_persist_until_finished|mtf_culture_3|mtf_sit_killed, 0),
#  ("killed_by_neutral", "killed_by_neutral.ogg", mtf_persist_until_finished|mtf_culture_6|mtf_sit_killed, 0),
#  ("killed_by_nord", "killed_by_nord.ogg", mtf_persist_until_finished|mtf_culture_4|mtf_sit_killed, 0),
#  ("killed_by_rhodok", "killed_by_rhodok.ogg", mtf_persist_until_finished|mtf_culture_5|mtf_sit_killed, 0),
  ("killed_by_swadian", "ying.ogg", mtf_module_track|mtf_persist_until_finished|mtf_culture_1|mtf_sit_killed, 0),
#  ("killed_by_vaegir", "killed_by_vaegir.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_killed, 0),
  
  ("lords_hall_khergit", "gongting.ogg", mtf_module_track|mtf_culture_3|mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern|mtf_culture_all),
  ("lords_hall_nord", "jingdong.ogg", mtf_module_track|mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("lords_hall_swadian", "suzhan2.ogg", mtf_module_track|mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("lords_hall_rhodok", "mount_and_blade_title_screen.ogg", mtf_module_track|mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("lords_hall_vaegir", "lvxing_1.ogg", mtf_module_track|mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),

  ("mounted_snow_terrain_calm", "lvxing_1.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_night|mtf_sit_tavern),
  ("neutral_infiltration", "suzhan2.ogg", mtf_sit_town_infiltrate, 0),
  ("outdoor_beautiful_land", "mount_and_blade_title_screen.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_night|mtf_sit_tavern),
  ("retreat", "ying.ogg", mtf_persist_until_finished|mtf_sit_killed, 0),

  ("seige_neutral", "gongting.ogg", mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),#TU
  ("enter_the_juggernaut", "jingdong.ogg", mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),  
  ("siege_attempt", "shu1.ogg", mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),  
  ("crazy_battle_music", "jinyong.ogg", mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),
  
  ("tavern_1", "xia2.ogg", mtf_sit_tavern|mtf_sit_feast, 0),
  ("tavern_2", "ying.ogg", mtf_sit_tavern|mtf_sit_feast, 0),

  ("town_neutral", "yiyeshu.ogg", mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night),
  ("town_khergit", "lvxing_1.ogg", mtf_culture_3|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_nord", "lvxing_2.mp3", mtf_culture_4|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_rhodok", "suzhan2.ogg", mtf_culture_5|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_swadian", "xia1.ogg", mtf_culture_1|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("town_vaegir", "jinyong.ogg", mtf_culture_2|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night|mtf_culture_all),

  ("travel_khergit", "lvxing_1.ogg", mtf_culture_3|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_neutral", "lvxing_2.mp3", mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
  ("travel_nord",    "lvxing_2.ogg",    mtf_culture_4|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_rhodok",  "travel2.ogg",  mtf_culture_5|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_swadian", "lvxing_1.ogg", mtf_culture_1|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_vaegir",  "lvxing_2.ogg",  mtf_culture_2|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("travel_sarranid",  "travel2.ogg",  mtf_culture_6|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),

  ("uncertain_homestead", "wolongyin.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("hearth_and_brotherhood", "xia1.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("tragic_village", "gongting.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),

  ("victorious_evil", "fight_as_wu.ogg", mtf_persist_until_finished, 0),
  ("victorious_neutral_1", "shu1.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),
  ("victorious_neutral_2", "mount_and_blade_title_screen.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),
  ("victorious_neutral_3", "jingdong.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),

  ("victorious_swadian", "lvxing_1.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious, 0),
  ("victorious_vaegir", "travel.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious, 0),
  ("victorious_vaegir_2", "jinyong.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious, 0),
  ("wedding", "wedding.ogg", mtf_persist_until_finished, 0),

  ("coronation", "jingdong.ogg", mtf_persist_until_finished, 0),



  
]
