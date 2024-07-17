from cachetools import cached
from cachetools.keys import hashkey

from ..consts.adaptative.regions import (
    CENTER_LARGE_V_REGION,
    CHAT_REGION,
    CONTENT_REGION,
    CONTENT_REGION_COLLECTABLE,
    CREATURE_MODE_REGION,
    CROSS_CONNECTIO_WARNING,
    CROSS_INFO_LOSE_FIGHT,
    CROSS_INFO_WIN_FIGHT,
    CROSS_MAP,
    CROSS_POPUP_INFO,
    CROSS_SALE_HOTEL_INVENTORY_RIGHT,
    END_FIGHT_MODAL_REGION,
    END_TURN_REGION,
    HELP_LOCK_FIGHT_PREP_REGION,
    ICON_CHARACTERISTIC_REGION,
    IN_FIGHT_REGION,
    INFO_MODAL_REGION,
    INVENTORY_RIGHT_CROSS_REGION,
    RIP_REGION,
    SALE_HOTEL_FILTER_CHECK_REGION,
    SALE_HOTEL_HUNDRED_QUANTITY_REGION,
    SALE_HOTEL_PLACE_SELL_REGION,
    SALE_HOTEL_TEN_QUANTITY_REGION,
)
from ..entities.object_search_config import CacheInfo, ObjectSearchConfig


class ObjectConfigs:
    in_game = ObjectSearchConfig(
        ref="in_game",
        lookup_region=ICON_CHARACTERISTIC_REGION,
        cache_info=CacheInfo(max_placement=2),
    )

    class Ankama:
        play = ObjectSearchConfig(
            ref="ankama.play", cache_info=CacheInfo(max_placement=2)
        )
        empty_play = ObjectSearchConfig(
            ref="ankama.empty_play", cache_info=CacheInfo(max_placement=2)
        )

    class Bank:
        owl_astrub = ObjectSearchConfig(
            lookup_region=CONTENT_REGION, ref="bank.owl_astrub"
        )
        owl_bonta = ObjectSearchConfig(
            lookup_region=CONTENT_REGION, ref="bank.owl_bonta"
        )
        consult_chest_text = ObjectSearchConfig(
            lookup_region=CONTENT_REGION, ref="bank.consult_chest_text"
        )
        transfer_icon_in = ObjectSearchConfig(
            threshold=0.95, ref="bank.transfer_icon_in"
        )
        transfer_icon_out = ObjectSearchConfig(
            lookup_region=CONTENT_REGION, ref="bank.transfer_icon_out"
        )
        transfer_all_text = ObjectSearchConfig(
            ref="bank.transfer_all_text",
            cache_info=CacheInfo(max_placement=None),
        )

    class Button:
        ok = ObjectSearchConfig(
            grey_scale=False, ref="button.ok", lookup_region=CENTER_LARGE_V_REGION
        )
        yes = ObjectSearchConfig(
            grey_scale=False,
            ref="button.yes",
            lookup_region=CENTER_LARGE_V_REGION,
            cache_info=CacheInfo(max_placement=2),
        )

    class Check:
        small = ObjectSearchConfig(
            lookup_region=CONTENT_REGION,
            grey_scale=False,
            threshold=0.95,
            ref="check.small",
            cache_info=CacheInfo(max_placement=2),
        )
        medium_inventory = ObjectSearchConfig(
            name="check.medium_inventory",
            lookup_region=SALE_HOTEL_FILTER_CHECK_REGION,
            ref="check.medium",
        )

    class Connection:
        launcher = ObjectSearchConfig(
            ref="connection.launcher", cache_info=CacheInfo(max_placement=2)
        )  # button can be shift
        play = ObjectSearchConfig(ref="connection.play")

    class Cross:
        green = ObjectSearchConfig(
            ref="cross.green",
            lookup_region=INFO_MODAL_REGION,
            cache_info=CacheInfo(max_placement=2),
        )
        inverted = ObjectSearchConfig(
            ref="cross.inverted", lookup_region=CENTER_LARGE_V_REGION
        )
        map = ObjectSearchConfig(ref="cross.map", lookup_region=CROSS_MAP)
        bank_inventory_right = ObjectSearchConfig(
            name="cross.bank_inventory_right",
            ref="cross.medium",
            lookup_region=INVENTORY_RIGHT_CROSS_REGION,
        )
        sale_hotel_inventory_right = ObjectSearchConfig(
            name="cross.sale_hotel_inventory_right",
            ref="cross.medium",
            lookup_region=CROSS_SALE_HOTEL_INVENTORY_RIGHT,
        )
        connection_warning = ObjectSearchConfig(
            name="cross.connection_warning",
            ref="cross.medium",
            lookup_region=CROSS_CONNECTIO_WARNING,
        )
        popup_info = ObjectSearchConfig(
            name="cross.popup_info",
            ref="cross.medium",
            lookup_region=CROSS_POPUP_INFO,
            cache_info=CacheInfo(max_placement=5),
        )
        info_win_fight = ObjectSearchConfig(
            name="cross.info_win_fight",
            ref="cross.small",
            lookup_region=CROSS_INFO_WIN_FIGHT,
            cache_info=CacheInfo(max_placement=2),
        )
        info_lose_fight = ObjectSearchConfig(
            name="cross.info_lose_fight",
            ref="cross.small",
            lookup_region=CROSS_INFO_LOSE_FIGHT,
            cache_info=CacheInfo(max_placement=2),
        )

    class Text:
        impossible_transfer = ObjectSearchConfig(
            grey_scale=False,
            threshold=0.95,
            ref="text.impossible_transfer",
            lookup_region=CHAT_REGION,
        )
        no_receipe = ObjectSearchConfig(
            ref="text.no_receipe", lookup_region=CONTENT_REGION
        )
        receipe = ObjectSearchConfig(ref="text.receipe", lookup_region=CONTENT_REGION)
        level_up = ObjectSearchConfig(
            grey_scale=False,
            ref="text.level_up",
            lookup_region=CONTENT_REGION,
            cache_info=None,
        )

    class Fight:
        ready = ObjectSearchConfig(lookup_region=END_TURN_REGION, ref="fight.ready")
        choose_chall = ObjectSearchConfig(
            lookup_region=END_TURN_REGION, ref="fight.prep.choose_chall"
        )
        in_prep = ObjectSearchConfig(
            lookup_region=HELP_LOCK_FIGHT_PREP_REGION, ref="fight.prep.in_prep"
        )
        lock = ObjectSearchConfig(
            lookup_region=HELP_LOCK_FIGHT_PREP_REGION,
            ref="fight.prep.lock",
            grey_scale=False,
            threshold=0.95,
        )
        end_turn = ObjectSearchConfig(
            lookup_region=END_TURN_REGION, threshold=0.95, ref="fight.end_turn"
        )
        mode_crea = ObjectSearchConfig(
            lookup_region=CREATURE_MODE_REGION,
            ref="fight.mode_crea",
            grey_scale=False,
            threshold=0.95,
        )
        enemy = ObjectSearchConfig(
            lookup_region=CONTENT_REGION,
            threshold=0.9,
            ref="fight.enemy",
            grey_scale=False,
            cache_info=None,
        )
        in_fight = ObjectSearchConfig(
            ref="fight.in_fight",
            threshold=0.9,
            lookup_region=IN_FIGHT_REGION,
            cache_info=None,
        )
        grave = ObjectSearchConfig(lookup_region=RIP_REGION, ref="fight.post.grave")
        phenix = ObjectSearchConfig(
            lookup_region=CONTENT_REGION,
            ref="fight.post.phenix",
            cache_info=CacheInfo(min_parsed_count_on_map=1),
        )
        defeat_text = ObjectSearchConfig(
            lookup_region=END_FIGHT_MODAL_REGION, ref="fight.post.defeat_text"
        )
        ressuscite_text = ObjectSearchConfig(
            lookup_region=CHAT_REGION, ref="fight.post.ressuscite_text", cache_info=None
        )

    class Harvest:
        impossible_recolt_text = ObjectSearchConfig(
            lookup_region=INFO_MODAL_REGION,
            ref="harvest.impossible_recolt_text",
            cache_info=CacheInfo(max_placement=2),
        )

    class Job:
        level_up = ObjectSearchConfig(
            threshold=0.9,
            ref="job.level_up",
            lookup_region=INFO_MODAL_REGION,
            cache_info=CacheInfo(max_placement=2),
        )

    class SaleHotel:
        on_place_in_sale = ObjectSearchConfig(
            lookup_region=SALE_HOTEL_PLACE_SELL_REGION,
            ref="sale_hotel.on_place_in_sale",
            threshold=0.95,
            grey_scale=False,
        )
        cant_place_text = ObjectSearchConfig(
            grey_scale=False, ref="sale_hotel.cant_place_text"
        )
        sale_category = ObjectSearchConfig(
            threshold=0.95, ref="sale_hotel.sale_category"
        )
        ten_quantity = ObjectSearchConfig(
            threshold=0.95,
            ref="sale_hotel.ten_quantity",
            lookup_region=SALE_HOTEL_TEN_QUANTITY_REGION,
        )
        hundred_quantity = ObjectSearchConfig(
            threshold=0.95,
            ref="sale_hotel.hundred_quantity",
            lookup_region=SALE_HOTEL_HUNDRED_QUANTITY_REGION,
        )

    class PathFinding:
        zaapi = ObjectSearchConfig(
            ref="path_finding.zaapi",
            cache_info=CacheInfo(min_parsed_count_on_map=1, max_placement=None),
        )
        lotery_havre_sac = ObjectSearchConfig(
            ref="path_finding.lotery_havre_sac", lookup_region=CONTENT_REGION
        )
        teleport_zaap = ObjectSearchConfig(
            ref="path_finding.teleport_zaap", lookup_region=CONTENT_REGION
        )

    class WorkShop:
        material_woodcutter = ObjectSearchConfig(
            threshold=0.95,
            ref="workshop.material_woodcutter",
            lookup_region=CONTENT_REGION,
            cache_info=CacheInfo(min_parsed_count_on_map=1),
        )
        material_alchimist = ObjectSearchConfig(
            threshold=0.95,
            ref="workshop.material_alchimist",
            lookup_region=CONTENT_REGION,
            cache_info=CacheInfo(min_parsed_count_on_map=1),
        )
        material_fisher = ObjectSearchConfig(
            threshold=0.95,
            ref="workshop.material_fisher",
            lookup_region=CONTENT_REGION,
            cache_info=CacheInfo(min_parsed_count_on_map=1),
        )
        material_peasant = ObjectSearchConfig(
            threshold=0.95,
            ref="workshop.material_peasant",
            lookup_region=CONTENT_REGION,
            cache_info=CacheInfo(min_parsed_count_on_map=1),
        )

    class Collectable:
        ble = ObjectSearchConfig(
            ref="collectable.ble",
            grey_scale=False,
            threshold=0.8,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        orge = ObjectSearchConfig(
            ref="collectable.orge",
            grey_scale=False,
            threshold=0.65,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        avoine = ObjectSearchConfig(
            ref="collectable.avoine",
            grey_scale=False,
            threshold=0.55,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        houblon = ObjectSearchConfig(
            ref="collectable.houblon",
            grey_scale=False,
            threshold=0.65,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        lin = ObjectSearchConfig(
            ref="collectable.lin",
            grey_scale=False,
            threshold=0.7,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        seigle = ObjectSearchConfig(
            ref="collectable.seigle",
            grey_scale=False,
            threshold=0.65,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        malt = ObjectSearchConfig(
            ref="collectable.malt",
            grey_scale=False,
            threshold=0.65,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        chanvre = ObjectSearchConfig(
            ref="collectable.chanvre",
            grey_scale=False,
            threshold=0.6,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        mais = ObjectSearchConfig(
            ref="collectable.mais",
            grey_scale=False,
            threshold=0.6,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        frostiz = ObjectSearchConfig(
            ref="collectable.frostiz",
            grey_scale=False,
            threshold=0.6,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        ortie = ObjectSearchConfig(
            ref="collectable.ortie",
            grey_scale=False,
            threshold=0.8,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        sauge = ObjectSearchConfig(
            ref="collectable.sauge",
            grey_scale=False,
            threshold=0.75,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        trefle_a_5_feuilles = ObjectSearchConfig(
            ref="collectable.trefle_a_5_feuilles",
            grey_scale=False,
            threshold=0.6,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        menthe_sauvage = ObjectSearchConfig(
            ref="collectable.menthe_sauvage",
            grey_scale=False,
            threshold=0.6,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        orchidee_freyesque = ObjectSearchConfig(
            ref="collectable.orchidee_freyesque",
            grey_scale=False,
            threshold=0.7,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        edelweiss = ObjectSearchConfig(
            ref="collectable.edelweiss",
            grey_scale=False,
            threshold=0.7,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        ginseng = ObjectSearchConfig(
            ref="collectable.ginseng",
            grey_scale=False,
            threshold=0.75,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        belladone = ObjectSearchConfig(
            ref="collectable.belladone",
            grey_scale=False,
            threshold=0.7,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        perce_neige = ObjectSearchConfig(
            ref="collectable.perce_neige",
            grey_scale=False,
            threshold=0.75,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        bois_de_frene = ObjectSearchConfig(
            ref="collectable.bois_de_frene",
            grey_scale=False,
            threshold=0.85,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        bois_de_chataignier = ObjectSearchConfig(
            ref="collectable.bois_de_chataignier",
            grey_scale=False,
            threshold=0.8,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        bois_de_noyer = ObjectSearchConfig(
            ref="collectable.bois_de_noyer",
            grey_scale=False,
            threshold=0.75,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        bois_de_chene = ObjectSearchConfig(
            ref="collectable.bois_de_chene",
            grey_scale=False,
            threshold=0.8,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        bois_de_bombu = ObjectSearchConfig(
            ref="collectable.bois_de_bombu",
            grey_scale=False,
            threshold=0.85,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        bois_d_erable = ObjectSearchConfig(
            ref="collectable.bois_d_erable",
            grey_scale=False,
            threshold=0.75,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        bois_d_if = ObjectSearchConfig(
            ref="collectable.bois_d_if",
            grey_scale=False,
            threshold=0.6,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        bois_de_merisier = ObjectSearchConfig(
            ref="collectable.bois_de_merisier",
            grey_scale=False,
            threshold=0.75,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        bois_de_noisetier = ObjectSearchConfig(
            ref="collectable.bois_de_noisetier",
            grey_scale=False,
            threshold=0.75,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        bois_d_ebene = ObjectSearchConfig(
            ref="collectable.bois_d_ebene",
            grey_scale=False,
            threshold=0.8,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        bois_de_charme = ObjectSearchConfig(
            ref="collectable.bois_de_charme",
            grey_scale=False,
            threshold=0.65,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        bois_d_orme = ObjectSearchConfig(
            ref="collectable.bois_d_orme",
            grey_scale=False,
            threshold=0.85,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        bois_de_tremble = ObjectSearchConfig(
            ref="collectable.bois_de_tremble",
            grey_scale=False,
            threshold=0.85,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        small_fish = ObjectSearchConfig(
            ref="collectable.small_fish",
            grey_scale=False,
            threshold=0.65,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        medium_fish = ObjectSearchConfig(
            ref="collectable.medium_fish",
            grey_scale=False,
            threshold=0.55,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )
        big_fish = ObjectSearchConfig(
            ref="collectable.big_fish",
            grey_scale=False,
            threshold=0.55,
            lookup_region=CONTENT_REGION_COLLECTABLE,
            cache_info=CacheInfo(min_parsed_count_on_map=30, max_placement=None),
        )


@cached(cache={}, key=lambda _object: hashkey(_object))
def get_all_template_config_by_ref(
    _object: object = ObjectConfigs,
) -> dict[str, ObjectSearchConfig]:
    configs_by_ref: dict[str, ObjectSearchConfig] = {}
    for attr in dir(_object):
        if not attr.startswith("__"):
            res = getattr(_object, attr)
            if not isinstance(res, ObjectSearchConfig):
                configs_by_ref.update(get_all_template_config_by_ref(res))
            else:
                configs_by_ref[res.ref] = res
    return configs_by_ref


COLLECTABLE_CONFIG_BY_NAME: dict[str, ObjectSearchConfig] = {
    # Peasant
    "ble": ObjectConfigs.Collectable.ble,
    "orge": ObjectConfigs.Collectable.orge,
    "avoine": ObjectConfigs.Collectable.avoine,
    "houblon": ObjectConfigs.Collectable.houblon,
    "lin": ObjectConfigs.Collectable.lin,
    "seigle": ObjectConfigs.Collectable.seigle,
    "malt": ObjectConfigs.Collectable.malt,
    "chanvre": ObjectConfigs.Collectable.chanvre,
    "mais": ObjectConfigs.Collectable.mais,
    "frostiz": ObjectConfigs.Collectable.frostiz,
    # Fisherman
    "goujon": ObjectConfigs.Collectable.small_fish,
    "greuvette": ObjectConfigs.Collectable.small_fish,
    "truite": ObjectConfigs.Collectable.small_fish,
    "crabe_sourimi": ObjectConfigs.Collectable.small_fish,
    "poisson_chaton": ObjectConfigs.Collectable.small_fish,
    "poisson_pane": ObjectConfigs.Collectable.small_fish,
    "carpe_d_iem": ObjectConfigs.Collectable.small_fish,
    "sardine_brillante": ObjectConfigs.Collectable.medium_fish,
    "brochet": ObjectConfigs.Collectable.medium_fish,
    "kralamoure": ObjectConfigs.Collectable.medium_fish,
    "anguille": ObjectConfigs.Collectable.medium_fish,
    "dorade_grise": ObjectConfigs.Collectable.medium_fish,
    "perche": ObjectConfigs.Collectable.medium_fish,
    "raie_bleue": ObjectConfigs.Collectable.medium_fish,
    "lotte": ObjectConfigs.Collectable.medium_fish,
    "requin_marteau_faucille": ObjectConfigs.Collectable.big_fish,
    "bar_rikain": ObjectConfigs.Collectable.big_fish,
    "morue": ObjectConfigs.Collectable.big_fish,
    "tanche": ObjectConfigs.Collectable.big_fish,
    "poisskaille": ObjectConfigs.Collectable.big_fish,
    # Woodcutter
    "bois_de_frene": ObjectConfigs.Collectable.bois_de_frene,
    "bois_de_chataignier": ObjectConfigs.Collectable.bois_de_chataignier,
    "bois_de_noyer": ObjectConfigs.Collectable.bois_de_noyer,
    "bois_de_chene": ObjectConfigs.Collectable.bois_de_chene,
    "bois_de_bombu": ObjectConfigs.Collectable.bois_de_bombu,
    "bois_d_erable": ObjectConfigs.Collectable.bois_d_erable,
    "bois_d_if": ObjectConfigs.Collectable.bois_d_if,
    "bois_de_merisier": ObjectConfigs.Collectable.bois_de_merisier,
    "bois_de_noisetier": ObjectConfigs.Collectable.bois_de_noisetier,
    "bois_de_charme": ObjectConfigs.Collectable.bois_de_charme,
    "bois_d_orme": ObjectConfigs.Collectable.bois_d_orme,
    "bois_de_tremble": ObjectConfigs.Collectable.bois_de_tremble,
    # Alchimist
    "ortie": ObjectConfigs.Collectable.ortie,
    "sauge": ObjectConfigs.Collectable.sauge,
    "trefle_a_5_feuilles": ObjectConfigs.Collectable.trefle_a_5_feuilles,
    "menthe_sauvage": ObjectConfigs.Collectable.menthe_sauvage,
    "orchidee_freyesque": ObjectConfigs.Collectable.orchidee_freyesque,
    "edelweiss": ObjectConfigs.Collectable.edelweiss,
    "ginseng": ObjectConfigs.Collectable.ginseng,
    "belladone": ObjectConfigs.Collectable.belladone,
    "perce_neige": ObjectConfigs.Collectable.perce_neige,
}
