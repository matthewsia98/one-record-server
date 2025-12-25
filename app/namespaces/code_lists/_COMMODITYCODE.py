from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class COMMODITYCODE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 02:55:58.740136
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/CommodityCode#")

    _fail = True

    CHEM: URIRef  # Chemicals
    CHEM_CDGR: URIRef  # Chemicals - Dangerous
    CHEM_CLNG: URIRef  # Cleaning products
    CHEM_CNDG: URIRef  # Chemicals - Not dangerous
    CHEM_CNMD: URIRef  # Chemicals - Not Medical
    CHEM_COSM: URIRef  # Cosmetics
    CHEM_COSM_COSD: URIRef  # Cosmetics - DGR
    CHEM_COSM_PERF: URIRef  # Perfume
    CHEM_DGRG: URIRef  # Dangerous Goods
    CHEM_DGRG_EXPL: URIRef  # Explosives
    CHEM_DICE: URIRef  # Dry ice
    CHEM_PAIN: URIRef  # Paint
    CHEM_PETRO: URIRef  # Petroleum derivatives
    CHEM_RADA: URIRef  # Radioactive materials
    CHEM_REAG: URIRef  # Reagents
    CONS: URIRef  # Consumer goods
    CONS_CMPY: URIRef  # Company material
    CONS_CWRE: URIRef  # Chinaware and Ceramics
    CONS_DIPL: URIRef  # Diplomatic mail and goods
    CONS_EXHB: URIRef  # Exhibition goods
    CONS_FRNT: URIRef  # Furniture
    CONS_GLAS: URIRef  # Glassware
    CONS_HAID: URIRef  # Humanitarian aid
    CONS_HHGD: URIRef  # Household goods
    CONS_HRSE: URIRef  # Horse equipment
    CONS_HSER: URIRef  # House removal
    CONS_OFSP: URIRef  # Office supplies
    CONS_PERS: URIRef  # Personal effects
    CONS_SPEC: URIRef  # Spectacles
    CONS_SPRT: URIRef  # Sports equipment
    CONS_TOYS: URIRef  # Toys and Games
    CONS_UBAG: URIRef  # Unaccompagnied baggage
    ELEC: URIRef  # Electronic equipment
    ELEC_AVEQ: URIRef  # Audio-Video-HiFi equipment
    ELEC_CALC: URIRef  # Calculators
    ELEC_CMPT: URIRef  # Computers
    ELEC_CPRT: URIRef  # Computer parts
    ELEC_ECOM: URIRef  # Electronic components
    ELEC_EEQP: URIRef  # Electronic equipment
    ELEC_EGDS: URIRef  # Electronic goods
    ELEC_ELQP: URIRef  # Electrical equipment
    ELEC_OFEQ: URIRef  # Office equipment
    ELEC_QUAN: URIRef  # Quantum
    ELEC_TELC: URIRef  # Telecom equipment
    FLWR: URIRef  # Plants, Flowers, Seeds
    FLWR_FLWR: URIRef  # Fresh flowers
    FLWR_FLWR_CFLW: URIRef  # Cut flowers
    FLWR_FLWR_TFLW: URIRef  # Tropical flowers
    FLWR_FLWR_TULP: URIRef  # Fresh tulips
    FLWR_FMNT: URIRef  # Fresh mint
    FLWR_HERBS: URIRef  # Herbs, Leaves and Foliage
    FLWR_PLNT: URIRef  # Plants
    FLWR_PLNT_APLN: URIRef  # Aquatic plants
    FLWR_PLNT_BULB: URIRef  # Bulbs and Tubers
    FLWR_PLNT_MPLN: URIRef  # Medicinal plants
    FLWR_PLNT_TPLN: URIRef  # Tropical plants
    FLWR_SEED: URIRef  # Seeds
    FOOD: URIRef  # Foodstuffs, Drinks and Tobacco
    FOOD_BVRG: URIRef  # Beverages
    FOOD_BVRG_BEER: URIRef  # Beer
    FOOD_BVRG_COFY: URIRef  # Coffee
    FOOD_BVRG_TEA: URIRef  # Tea
    FOOD_BVRG_WINE: URIRef  # Wine
    FOOD_CERE: URIRef  # Cereal foods
    FOOD_CERE_BRED: URIRef  # Bread
    FOOD_CERE_CAKE: URIRef  # Cakes and Pastries
    FOOD_DARY: URIRef  # Dairy products
    FOOD_DARY_CHSE: URIRef  # Cheese
    FOOD_DARY_EGGS: URIRef  # Eggs
    FOOD_DARY_ICEC: URIRef  # Ice cream
    FOOD_FISH: URIRef  # Fish and Seafood
    FOOD_FISH_ALBA: URIRef  # Albacora
    FOOD_FISH_CAVR: URIRef  # Caviar
    FOOD_FISH_FFSH: URIRef  # Fresh fish
    FOOD_FISH_FRZF: URIRef  # Frozen fish
    FOOD_FISH_FRZS: URIRef  # Frozen seafood
    FOOD_FISH_HAKE: URIRef  # Hake
    FOOD_FISH_LOBS: URIRef  # Lobsters and Crabs
    FOOD_FISH_REPA: URIRef  # Reineta and Palometa
    FOOD_FISH_SFIN: URIRef  # Shark fin
    FOOD_FISH_SFSH: URIRef  # Smoked fish
    FOOD_FISH_SHRI: URIRef  # Shrimps and Prawns
    FOOD_FISH_SLMN: URIRef  # Salmon
    FOOD_FISH_TUNA: URIRef  # Tuna
    FOOD_FRTV: URIRef  # Fruits and Vegetables
    FOOD_FRTV_APPL: URIRef  # Apples
    FOOD_FRTV_ASPA: URIRef  # Asparagus
    FOOD_FRTV_AVOC: URIRef  # Avocados
    FOOD_FRTV_BANA: URIRef  # Bananas
    FOOD_FRTV_BEAN: URIRef  # String beans
    FOOD_FRTV_BERR: URIRef  # Berries
    FOOD_FRTV_CHER: URIRef  # Cherries
    FOOD_FRTV_CMBR: URIRef  # Cucumber
    FOOD_FRTV_DURI: URIRef  # Durian
    FOOD_FRTV_GARL: URIRef  # Garlic
    FOOD_FRTV_GRAP: URIRef  # Grapes
    FOOD_FRTV_LITC: URIRef  # Litchies
    FOOD_FRTV_MANG: URIRef  # Mangoes
    FOOD_FRTV_MLNS: URIRef  # Melons
    FOOD_FRTV_MUSH: URIRef  # Mushrooms
    FOOD_FRTV_PEPP: URIRef  # Peppers
    FOOD_FRTV_PINE: URIRef  # Pineapple
    FOOD_FRTV_PPYA: URIRef  # Papaya
    FOOD_FRTV_PROD: URIRef  # Produce
    FOOD_FRTV_STRW: URIRef  # Strawberries
    FOOD_FRTV_TOMA: URIRef  # Tomatoes
    FOOD_MEAT: URIRef  # Meat products
    FOOD_MEAT_BEEF: URIRef  # Beef products
    FOOD_MEAT_DRIM: URIRef  # Dried meat
    FOOD_MEAT_FRZM: URIRef  # Frozen meat
    FOOD_MEAT_GOSL: URIRef  # Goose liver
    FOOD_MEAT_GUTS: URIRef  # Guts
    FOOD_MEAT_HRSP: URIRef  # Horse products
    FOOD_MEAT_MEAT: URIRef  # Meat
    FOOD_MEAT_PORK: URIRef  # Pork products
    FOOD_MEAT_SAUS: URIRef  # Sausages
    FOOD_PERI: URIRef  # Perhishables
    FOOD_STUF: URIRef  # Foodstuffs
    FOOD_STUF_CATE: URIRef  # Catering products
    FOOD_STUF_CHOC: URIRef  # Chocolate
    FOOD_STUF_DFRU: URIRef  # Dried fruit
    FOOD_STUF_MPWD: URIRef  # Milk powder
    FOOD_STUF_NUTS: URIRef  # Nuts
    FOOD_STUF_OOIL: URIRef  # Olive oil
    FOOD_STUF_SPCE: URIRef  # Spices and Roots
    FOOD_TBCO: URIRef  # Tobacco products
    FOOD_TBCO_CGRT: URIRef  # Cigarettes
    FOOD_TBCO_CIGA: URIRef  # Cigars
    GENE: URIRef  # General Cargo
    HUMR: URIRef  # Human Remains
    HUMR_HUMB: URIRef  # Human remains not cremated
    HUMR_HUMC: URIRef  # Human remains cremated
    LIVE: URIRef  # Live Animals
    LIVE_BRDH: URIRef  # Birds & Hatching Eggs
    LIVE_BRDH_BIRD: URIRef  # Birds
    LIVE_BRDH_CHIC: URIRef  # Chicks
    LIVE_BRDH_DUCK: URIRef  # Ducks
    LIVE_BRDH_HEGG: URIRef  # Hatching Eggs
    LIVE_BRDH_OSTR: URIRef  # Ostriches
    LIVE_BRDH_PARR: URIRef  # Parrots
    LIVE_BRDH_TRKY: URIRef  # Turkeys
    LIVE_INSC: URIRef  # Insects
    LIVE_INSC_BEES: URIRef  # Bees
    LIVE_LFSH: URIRef  # Fish
    LIVE_LFSH_EELS: URIRef  # Eels
    LIVE_LFSH_KOIF: URIRef  # Koi fish
    LIVE_LFSH_TRPF: URIRef  # Tropical fish
    LIVE_MLKS: URIRef  # Mollusks
    LIVE_MLKS_LUGW: URIRef  # Lugworms
    LIVE_MLKS_SNAI: URIRef  # Snails
    LIVE_MMLS: URIRef  # Mammals
    LIVE_MMLS_CATL: URIRef  # Cattle
    LIVE_MMLS_CATS: URIRef  # Cats
    LIVE_MMLS_CATS_Abyssinian: URIRef  # Abyssinian
    LIVE_MMLS_CATS_American_Bobtail: URIRef  # American Bobtail
    LIVE_MMLS_CATS_American_Curl: URIRef  # American Curl
    LIVE_MMLS_CATS_American_Keuda: URIRef  # American Keuda
    LIVE_MMLS_CATS_American_Lynx: URIRef  # American Lynx
    LIVE_MMLS_CATS_American_Polydactyl: URIRef  # American Polydactyl
    LIVE_MMLS_CATS_American_Shorthair: URIRef  # American Shorthair
    LIVE_MMLS_CATS_American_Wirehair: URIRef  # American Wirehair
    LIVE_MMLS_CATS_Asian: URIRef  # Asian
    LIVE_MMLS_CATS_Australian_Mist: URIRef  # Australian Mist
    LIVE_MMLS_CATS_Balinese: URIRef  # Balinese
    LIVE_MMLS_CATS_Bengal: URIRef  # Bengal
    LIVE_MMLS_CATS_Birman: URIRef  # Birman
    LIVE_MMLS_CATS_Bombay: URIRef  # Bombay
    LIVE_MMLS_CATS_Bristol: URIRef  # Bristol
    LIVE_MMLS_CATS_British_Shorthair: URIRef  # British Shorthair
    LIVE_MMLS_CATS_Burmese: URIRef  # Burmese
    LIVE_MMLS_CATS_California_Spangled: URIRef  # California Spangled
    LIVE_MMLS_CATS_Chartreux: URIRef  # Chartreux
    LIVE_MMLS_CATS_Chausie: URIRef  # Chausie
    LIVE_MMLS_CATS_Chinese_Harlequin: URIRef  # Chinese Harlequin
    LIVE_MMLS_CATS_Color_Point_Shorthair: URIRef  # Color Point Shorthair
    LIVE_MMLS_CATS_Copper: URIRef  # Copper
    LIVE_MMLS_CATS_Cornish_Rex: URIRef  # Cornish Rex
    LIVE_MMLS_CATS_Cymric: URIRef  # Cymric
    LIVE_MMLS_CATS_Desert_Lynx: URIRef  # Desert Lynx
    LIVE_MMLS_CATS_Devon_Rex: URIRef  # Devon Rex
    LIVE_MMLS_CATS_Donskoy: URIRef  # Donskoy
    LIVE_MMLS_CATS_Egyptian_Mau: URIRef  # Egyptian Mau
    LIVE_MMLS_CATS_Exotic_Shorthair: URIRef  # Exotic Shorthair
    LIVE_MMLS_CATS_Havana: URIRef  # Havana
    LIVE_MMLS_CATS_Highland_Lynx: URIRef  # Highland Lynx
    LIVE_MMLS_CATS_Himalayan: URIRef  # Himalayan
    LIVE_MMLS_CATS_Japanese_Bobtail: URIRef  # Japanese Bobtail
    LIVE_MMLS_CATS_Javanese: URIRef  # Javanese
    LIVE_MMLS_CATS_Korat: URIRef  # Korat
    LIVE_MMLS_CATS_LaPerm: URIRef  # LaPerm
    LIVE_MMLS_CATS_Maine_Coon: URIRef  # Maine Coon
    LIVE_MMLS_CATS_Manx: URIRef  # Manx
    LIVE_MMLS_CATS_Mojave_Spotted: URIRef  # Mojave Spotted
    LIVE_MMLS_CATS_Munchkin: URIRef  # Munchkin
    LIVE_MMLS_CATS_Niebelung: URIRef  # Niebelung
    LIVE_MMLS_CATS_Norwegian_Forest: URIRef  # Norwegian Forest
    LIVE_MMLS_CATS_Ocicat: URIRef  # Ocicat
    LIVE_MMLS_CATS_Ojos_Azules: URIRef  # Ojos Azules
    LIVE_MMLS_CATS_Oriental: URIRef  # Oriental
    LIVE_MMLS_CATS_Pantherette: URIRef  # Pantherette
    LIVE_MMLS_CATS_Persian: URIRef  # Persian
    LIVE_MMLS_CATS_Peterbald: URIRef  # Peterbald
    LIVE_MMLS_CATS_Pixiebob: URIRef  # Pixiebob
    LIVE_MMLS_CATS_Ragamuffin: URIRef  # Ragamuffin
    LIVE_MMLS_CATS_Ragdoll: URIRef  # Ragdoll
    LIVE_MMLS_CATS_Russian_Blue: URIRef  # Russian Blue
    LIVE_MMLS_CATS_Safari: URIRef  # Safari
    LIVE_MMLS_CATS_Savannah: URIRef  # Savannah
    LIVE_MMLS_CATS_Scottish_Fold: URIRef  # Scottish Fold
    LIVE_MMLS_CATS_Selkirk_Rex: URIRef  # Selkirk Rex
    LIVE_MMLS_CATS_Serengeti: URIRef  # Serengeti
    LIVE_MMLS_CATS_Siamese: URIRef  # Siamese
    LIVE_MMLS_CATS_Siberian: URIRef  # Siberian
    LIVE_MMLS_CATS_Singapura: URIRef  # Singapura
    LIVE_MMLS_CATS_Snowshoe: URIRef  # Snowshoe
    LIVE_MMLS_CATS_Somali: URIRef  # Somali
    LIVE_MMLS_CATS_Sphynx: URIRef  # Sphynx
    LIVE_MMLS_CATS_Tiffany: URIRef  # Tiffany
    LIVE_MMLS_CATS_Tonkinese: URIRef  # Tonkinese
    LIVE_MMLS_CATS_Traditional_Siamese: URIRef  # Traditional Siamese
    LIVE_MMLS_CATS_Turkish_Angora: URIRef  # Turkish Angora
    LIVE_MMLS_CATS_Turkish_Van: URIRef  # Turkish Van
    LIVE_MMLS_CATS_Vienna_Woods: URIRef  # Vienna Woods
    LIVE_MMLS_CATS_Viverral_Hybrid_Cat: URIRef  # Viverral-Hybrid Cat
    LIVE_MMLS_CATS_York_Chocolate: URIRef  # York Chocolate
    LIVE_MMLS_DOGS: URIRef  # Dogs
    LIVE_MMLS_DOGS_Affenpinscher: URIRef  # Affenpinscher
    LIVE_MMLS_DOGS_Afghan_Hound: URIRef  # Afghan Hound
    LIVE_MMLS_DOGS_Airedale_Terrier: URIRef  # Airedale Terrier
    LIVE_MMLS_DOGS_Akita: URIRef  # Akita
    LIVE_MMLS_DOGS_Alangu_Mastiff: URIRef  # Alangu Mastiff
    LIVE_MMLS_DOGS_Alano: URIRef  # Alano
    LIVE_MMLS_DOGS_Alaskan_Malamute: URIRef  # Alaskan Malamute
    LIVE_MMLS_DOGS_American_Bulldog: URIRef  # American Bulldog
    LIVE_MMLS_DOGS_American_Bully: URIRef  # American Bully
    LIVE_MMLS_DOGS_American_Cocker_Spaniel: URIRef  # American Cocker Spaniel
    LIVE_MMLS_DOGS_American_English_Coonhound: URIRef  # American English Coonhound
    LIVE_MMLS_DOGS_American_Eskimo_Dog_Miniature: (
        URIRef  # American Eskimo Dog-Miniature
    )
    LIVE_MMLS_DOGS_American_Eskimo_Dog_Standard: URIRef  # American Eskimo Dog-Standard
    LIVE_MMLS_DOGS_American_Eskimo_Dog_Toy: URIRef  # American Eskimo Dog-Toy
    LIVE_MMLS_DOGS_American_Foxhound: URIRef  # American Foxhound
    LIVE_MMLS_DOGS_American_Hairless_Terrier: URIRef  # American Hairless Terrier
    LIVE_MMLS_DOGS_American_Pit_Bull_Terrier: URIRef  # American Pit Bull Terrier
    LIVE_MMLS_DOGS_American_Staffordshire_Terrier: (
        URIRef  # American Staffordshire Terrier
    )
    LIVE_MMLS_DOGS_American_Water_Spaniel: URIRef  # American Water Spaniel
    LIVE_MMLS_DOGS_Anatolian_Shepherd_Dog: URIRef  # Anatolian Shepherd Dog
    LIVE_MMLS_DOGS_Argentinian_Mastiff: URIRef  # Argentinian Mastiff
    LIVE_MMLS_DOGS_Aussiedoodle: URIRef  # Aussiedoodle
    LIVE_MMLS_DOGS_Australian_Cattle_Dog: URIRef  # Australian Cattle Dog
    LIVE_MMLS_DOGS_Australian_Shepherd: URIRef  # Australian Shepherd
    LIVE_MMLS_DOGS_Australian_Terrier: URIRef  # Australian Terrier
    LIVE_MMLS_DOGS_Ba_Shar_Basset_Hound_Shar_pei_Mix: (
        URIRef  # Ba Shar-Basset Hound Shar pei Mix
    )
    LIVE_MMLS_DOGS_Basenji: URIRef  # Basenji
    LIVE_MMLS_DOGS_Basset_Hound: URIRef  # Basset Hound
    LIVE_MMLS_DOGS_Beagle: URIRef  # Beagle
    LIVE_MMLS_DOGS_Bearded_Collie: URIRef  # Bearded Collie
    LIVE_MMLS_DOGS_Beauceron: URIRef  # Beauceron
    LIVE_MMLS_DOGS_Bedlington_Terrier: URIRef  # Bedlington Terrier
    LIVE_MMLS_DOGS_Belgian_Malinois: URIRef  # Belgian Malinois
    LIVE_MMLS_DOGS_Belgian_Sheepdog: URIRef  # Belgian Sheepdog
    LIVE_MMLS_DOGS_Belgian_Tervuren: URIRef  # Belgian Tervuren
    LIVE_MMLS_DOGS_Bergamasco: URIRef  # Bergamasco
    LIVE_MMLS_DOGS_Berger_Picard: URIRef  # Berger Picard
    LIVE_MMLS_DOGS_Bernedoodle: URIRef  # Bernedoodle
    LIVE_MMLS_DOGS_Bernese_Mountain_Dog: URIRef  # Bernese Mountain Dog
    LIVE_MMLS_DOGS_Bichon_Frise: URIRef  # Bichon Frise
    LIVE_MMLS_DOGS_Black_Russian_Terrier: URIRef  # Black Russian Terrier
    LIVE_MMLS_DOGS_Black_and_Tan_Coonhound: URIRef  # Black and Tan Coonhound
    LIVE_MMLS_DOGS_Bloodhound: URIRef  # Bloodhound
    LIVE_MMLS_DOGS_Bluetick_Coonhound: URIRef  # Bluetick Coonhound
    LIVE_MMLS_DOGS_Boerboel: URIRef  # Boerboel
    LIVE_MMLS_DOGS_Border_Collie: URIRef  # Border Collie
    LIVE_MMLS_DOGS_Border_Terrier: URIRef  # Border Terrier
    LIVE_MMLS_DOGS_Borzoi: URIRef  # Borzoi
    LIVE_MMLS_DOGS_Boston_Terrier: URIRef  # Boston Terrier
    LIVE_MMLS_DOGS_Bouvier_des_Flandres: URIRef  # Bouvier des Flandres
    LIVE_MMLS_DOGS_Boweimar_Boxer_Weimaraner_Mix: (
        URIRef  # Boweimar-Boxer Weimaraner Mix
    )
    LIVE_MMLS_DOGS_Boxer: URIRef  # Boxer
    LIVE_MMLS_DOGS_Boykin_Spaniel: URIRef  # Boykin Spaniel
    LIVE_MMLS_DOGS_Brazilian_Mastiff: URIRef  # Brazilian Mastiff
    LIVE_MMLS_DOGS_Briard: URIRef  # Briard
    LIVE_MMLS_DOGS_Brittany: URIRef  # Brittany
    LIVE_MMLS_DOGS_Brussels_Griffon: URIRef  # Brussels Griffon
    LIVE_MMLS_DOGS_Bull_Terrier: URIRef  # Bull Terrier
    LIVE_MMLS_DOGS_Bull_Terrier_Miniature: URIRef  # Bull Terrier-Miniature
    LIVE_MMLS_DOGS_Bulldog: URIRef  # Bulldog
    LIVE_MMLS_DOGS_Bulli_Kutta: URIRef  # Bulli Kutta
    LIVE_MMLS_DOGS_Bullmastiff: URIRef  # Bullmastiff
    LIVE_MMLS_DOGS_Bully_Kutta_Mastiff_breed: URIRef  # Bully Kutta-Mastiff breed
    LIVE_MMLS_DOGS_Cairn_Terrier: URIRef  # Cairn Terrier
    LIVE_MMLS_DOGS_Campeiro_Bulldog_Brazilian_Bulldog: (
        URIRef  # Campeiro Bulldog-Brazilian Bulldog
    )
    LIVE_MMLS_DOGS_Canaan_Dog: URIRef  # Canaan Dog
    LIVE_MMLS_DOGS_Canary_Mastiff: URIRef  # Canary Mastiff
    LIVE_MMLS_DOGS_Cane_Corso: URIRef  # Cane Corso
    LIVE_MMLS_DOGS_Cardigan_Welsh_Corgi: URIRef  # Cardigan Welsh Corgi
    LIVE_MMLS_DOGS_Catahoula_Bulldog_Catahoula_Leopard_Bulldog: (
        URIRef  # Catahoula Bulldog-Catahoula Leopard Bulldog
    )
    LIVE_MMLS_DOGS_Cavachon_King_Charles_Spaniel_Bichon_Frise: (
        URIRef  # Cavachon-King Charles Spaniel Bichon Frise
    )
    LIVE_MMLS_DOGS_Cavalier_King_Charles_Spaniel: (
        URIRef  # Cavalier King Charles Spaniel
    )
    LIVE_MMLS_DOGS_Cavapoo_Cavalier_King_Charles_Spaniel_Poodle: (
        URIRef  # Cavapoo-Cavalier King Charles Spaniel Poodle
    )
    LIVE_MMLS_DOGS_Cesky_Terrier: URIRef  # Cesky Terrier
    LIVE_MMLS_DOGS_Chesapeake_Bay_Retriever: URIRef  # Chesapeake Bay Retriever
    LIVE_MMLS_DOGS_Chihuahua: URIRef  # Chihuahua
    LIVE_MMLS_DOGS_Chinese_Crested_Dog: URIRef  # Chinese Crested Dog
    LIVE_MMLS_DOGS_Chinese_Pug: URIRef  # Chinese Pug
    LIVE_MMLS_DOGS_Chinese_Shar_Pei: URIRef  # Chinese Shar Pei
    LIVE_MMLS_DOGS_Chinook: URIRef  # Chinook
    LIVE_MMLS_DOGS_Chipin_Chihuahua_Minature_Pinscher_Mix: (
        URIRef  # Chipin-Chihuahua Minature Pinscher Mix
    )
    LIVE_MMLS_DOGS_Chiweenie_Chihuahua_Dachshund_Mix: (
        URIRef  # Chiweenie-Chihuahua Dachshund Mix
    )
    LIVE_MMLS_DOGS_Chorkie_Chihuahua_Yorkshire_Terrier_Mix: (
        URIRef  # Chorkie-Chihuahua Yorkshire Terrier Mix
    )
    LIVE_MMLS_DOGS_Chow_Chow: URIRef  # Chow Chow
    LIVE_MMLS_DOGS_Chow_Pei_Chow_Chow_Shar_Pei_Mix: (
        URIRef  # Chow Pei-Chow Chow Shar Pei Mix
    )
    LIVE_MMLS_DOGS_Cirneco_dell_Etna: URIRef  # Cirneco dell Etna
    LIVE_MMLS_DOGS_Clumber_Spaniel: URIRef  # Clumber Spaniel
    LIVE_MMLS_DOGS_Cockapoo_Cocker_Spaniel_Poodle_Mix: (
        URIRef  # Cockapoo-Cocker Spaniel Poodle Mix
    )
    LIVE_MMLS_DOGS_Cocker_Spaniel: URIRef  # Cocker Spaniel
    LIVE_MMLS_DOGS_Collie: URIRef  # Collie
    LIVE_MMLS_DOGS_Coton_de_Tulear: URIRef  # Coton de Tulear
    LIVE_MMLS_DOGS_Curly_Coated_Retriever: URIRef  # Curly-Coated Retriever
    LIVE_MMLS_DOGS_Dachshund: URIRef  # Dachshund
    LIVE_MMLS_DOGS_Dalmatian: URIRef  # Dalmatian
    LIVE_MMLS_DOGS_Dandie_Dinmont_Terrier: URIRef  # Dandie Dinmont Terrier
    LIVE_MMLS_DOGS_Doberman_Pinscher: URIRef  # Doberman Pinscher
    LIVE_MMLS_DOGS_Dogo_Argentino: URIRef  # Dogo Argentino
    LIVE_MMLS_DOGS_Dogue_de_Bordeaux: URIRef  # Dogue de Bordeaux
    LIVE_MMLS_DOGS_Doxiepoo_Dachshund_Poodle_Mix: (
        URIRef  # Doxiepoo-Dachshund Poodle Mix
    )
    LIVE_MMLS_DOGS_Dutch_Pug: URIRef  # Dutch Pug
    LIVE_MMLS_DOGS_English_Bulldog: URIRef  # English Bulldog
    LIVE_MMLS_DOGS_English_Cocker_Spaniel: URIRef  # English Cocker Spaniel
    LIVE_MMLS_DOGS_English_Foxhound: URIRef  # English Foxhound
    LIVE_MMLS_DOGS_English_Mastiff: URIRef  # English Mastiff
    LIVE_MMLS_DOGS_English_Setter: URIRef  # English Setter
    LIVE_MMLS_DOGS_English_Springer_Spaniel: URIRef  # English Springer Spaniel
    LIVE_MMLS_DOGS_English_Toy_Spaniel: URIRef  # English Toy Spaniel
    LIVE_MMLS_DOGS_Entlebucher_Mountain_Dog: URIRef  # Entlebucher Mountain Dog
    LIVE_MMLS_DOGS_Eurasier: URIRef  # Eurasier
    LIVE_MMLS_DOGS_Field_Spaniel: URIRef  # Field Spaniel
    LIVE_MMLS_DOGS_Fila_Brasileiro_Brazilian_Mastiff: (
        URIRef  # Fila Brasileiro-Brazilian Mastiff
    )
    LIVE_MMLS_DOGS_Finnish_Lapphund: URIRef  # Finnish Lapphund
    LIVE_MMLS_DOGS_Finnish_Spitz: URIRef  # Finnish Spitz
    LIVE_MMLS_DOGS_Flat_Coated_Retriever: URIRef  # Flat-Coated Retriever
    LIVE_MMLS_DOGS_French_Bulldog: URIRef  # French Bulldog
    LIVE_MMLS_DOGS_French_Mastiff: URIRef  # French Mastiff
    LIVE_MMLS_DOGS_German_Mastiff_Great_Dane: URIRef  # German Mastiff-Great Dane
    LIVE_MMLS_DOGS_German_Pinscher: URIRef  # German Pinscher
    LIVE_MMLS_DOGS_German_Shepherd_Dog: URIRef  # German Shepherd Dog
    LIVE_MMLS_DOGS_German_Shorthaired_Pointer: URIRef  # German Shorthaired Pointer
    LIVE_MMLS_DOGS_German_Wirehaired_Pointer: URIRef  # German Wirehaired Pointer
    LIVE_MMLS_DOGS_Giant_Schnauzer: URIRef  # Giant Schnauzer
    LIVE_MMLS_DOGS_Glen_of_Imaal_Terrier: URIRef  # Glen of Imaal Terrier
    LIVE_MMLS_DOGS_Goldador_Golden_Retriever_Labrador_Retriever: (
        URIRef  # Goldador-Golden Retriever Labrador Retriever
    )
    LIVE_MMLS_DOGS_Golden_Retriever: URIRef  # Golden Retriever
    LIVE_MMLS_DOGS_Goldendoodle_Golden_Retriever_Poodle_Mix: (
        URIRef  # Goldendoodle-Golden Retriever Poodle Mix
    )
    LIVE_MMLS_DOGS_Gordon_Setter: URIRef  # Gordon Setter
    LIVE_MMLS_DOGS_Great_Dane: URIRef  # Great Dane
    LIVE_MMLS_DOGS_Great_Pyrenees: URIRef  # Great Pyrenees
    LIVE_MMLS_DOGS_Greater_Swiss_Mountain_Dog: URIRef  # Greater Swiss Mountain Dog
    LIVE_MMLS_DOGS_Greyhound: URIRef  # Greyhound
    LIVE_MMLS_DOGS_Harrier: URIRef  # Harrier
    LIVE_MMLS_DOGS_Havanese: URIRef  # Havanese
    LIVE_MMLS_DOGS_Ibizan_Hound: URIRef  # Ibizan Hound
    LIVE_MMLS_DOGS_Icelandic_Sheepdog: URIRef  # Icelandic Sheepdog
    LIVE_MMLS_DOGS_Irish_Red_and_White_Setter: URIRef  # Irish Red and White Setter
    LIVE_MMLS_DOGS_Irish_Setter: URIRef  # Irish Setter
    LIVE_MMLS_DOGS_Irish_Terrier: URIRef  # Irish Terrier
    LIVE_MMLS_DOGS_Irish_Water_Spaniel: URIRef  # Irish Water Spaniel
    LIVE_MMLS_DOGS_Irish_Wolfhound: URIRef  # Irish Wolfhound
    LIVE_MMLS_DOGS_Italian_Greyhound: URIRef  # Italian Greyhound
    LIVE_MMLS_DOGS_Italian_Mastiff: URIRef  # Italian Mastiff
    LIVE_MMLS_DOGS_Jack_Chi_Chihuahua_Jack_Russell_Terrier_Mix: (
        URIRef  # Jack Chi-Chihuahua Jack Russell Terrier Mix
    )
    LIVE_MMLS_DOGS_Jack_Russell_Terrier: URIRef  # Jack Russell Terrier
    LIVE_MMLS_DOGS_Japanese_Boxer: URIRef  # Japanese Boxer
    LIVE_MMLS_DOGS_Japanese_Chin: URIRef  # Japanese Chin
    LIVE_MMLS_DOGS_Japanese_Mastiff: URIRef  # Japanese Mastiff
    LIVE_MMLS_DOGS_Japanese_Pug: URIRef  # Japanese Pug
    LIVE_MMLS_DOGS_Japanese_Spaniel: URIRef  # Japanese Spaniel
    LIVE_MMLS_DOGS_Kangal_Shepherd_Dog: URIRef  # Kangal Shepherd Dog
    LIVE_MMLS_DOGS_Keeshond: URIRef  # Keeshond
    LIVE_MMLS_DOGS_Kerry_Blue_Terrier: URIRef  # Kerry Blue Terrier
    LIVE_MMLS_DOGS_King_Charles_Spaniel: URIRef  # King Charles Spaniel
    LIVE_MMLS_DOGS_Komondor: URIRef  # Komondor
    LIVE_MMLS_DOGS_Kuvasz: URIRef  # Kuvasz
    LIVE_MMLS_DOGS_Kyi_Leo_Maltese_Lhasa_Apso_Mix: (
        URIRef  # Kyi-Leo-Maltese Lhasa Apso Mix
    )
    LIVE_MMLS_DOGS_Labrabull_Labrador_Retriever_American_Pit_Bull: (
        URIRef  # Labrabull-Labrador Retriever American Pit Bull
    )
    LIVE_MMLS_DOGS_Labradane_Labrador_Retriever_Great_Dane_Mix: (
        URIRef  # Labradane-Labrador Retriever Great Dane Mix
    )
    LIVE_MMLS_DOGS_Labradoodle_Labrador_Retriever_Poodle_Mix: (
        URIRef  # Labradoodle Labrador Retriever Poodle Mix
    )
    LIVE_MMLS_DOGS_Labrador_Retriever: URIRef  # Labrador Retriever
    LIVE_MMLS_DOGS_Lagotto_Romagnolo: URIRef  # Lagotto Romagnolo
    LIVE_MMLS_DOGS_Lakeland_Terrier: URIRef  # Lakeland Terrier
    LIVE_MMLS_DOGS_Leonberger: URIRef  # Leonberger
    LIVE_MMLS_DOGS_Lhasa_Apso: URIRef  # Lhasa Apso
    LIVE_MMLS_DOGS_Löwchen: URIRef  # Löwchen
    LIVE_MMLS_DOGS_Mal_Shi_Maltese_Shih_Tzu_Mix: URIRef  # Mal-Shi-Maltese Shih Tzu Mix
    LIVE_MMLS_DOGS_Malt_Tzu_Maltese_Shih_Tzu_Mix: (
        URIRef  # Malt-Tzu-Maltese Shih Tzu Mix
    )
    LIVE_MMLS_DOGS_Maltese: URIRef  # Maltese
    LIVE_MMLS_DOGS_Maltese_Shih_Tzu: URIRef  # Maltese Shih Tzu
    LIVE_MMLS_DOGS_Malti_Zu_Maltese_Shih_Tzu_Mix: (
        URIRef  # Malti Zu-Maltese Shih Tzu Mix
    )
    LIVE_MMLS_DOGS_Maltipoo_Maltese_Poodle_Mix: URIRef  # Maltipoo-Maltese Poodle Mix
    LIVE_MMLS_DOGS_Manchester_Terrier: URIRef  # Manchester Terrier
    LIVE_MMLS_DOGS_Mastador_Bullmastiff_Labrador_Retriever_Mix: (
        URIRef  # Mastador-Bullmastiff Labrador Retriever Mix
    )
    LIVE_MMLS_DOGS_Mastiff: URIRef  # Mastiff
    LIVE_MMLS_DOGS_Mastin_Espanol_Spanish_Mastiff: (
        URIRef  # Mastin Espanol-Spanish Mastiff
    )
    LIVE_MMLS_DOGS_Mastino_Napoletano_Neopolitan_Mastiff: (
        URIRef  # Mastino Napoletano-Neopolitan Mastiff
    )
    LIVE_MMLS_DOGS_Miniature_American_Shepherd: URIRef  # Miniature American Shepherd
    LIVE_MMLS_DOGS_Miniature_Bull_Terrier: URIRef  # Miniature Bull Terrier
    LIVE_MMLS_DOGS_Miniature_Pinscher: URIRef  # Miniature Pinscher
    LIVE_MMLS_DOGS_Miniature_Schnauzer: URIRef  # Miniature Schnauzer
    LIVE_MMLS_DOGS_Mixed_Invalid_Breed_Type: URIRef  # Mixed-Invalid Breed Type
    LIVE_MMLS_DOGS_Neapolitan_Mastiff: URIRef  # Neapolitan Mastiff
    LIVE_MMLS_DOGS_Newfoundland: URIRef  # Newfoundland
    LIVE_MMLS_DOGS_Norfolk_Terrier: URIRef  # Norfolk Terrier
    LIVE_MMLS_DOGS_Norwegian_Buhund: URIRef  # Norwegian Buhund
    LIVE_MMLS_DOGS_Norwegian_Elkhound: URIRef  # Norwegian Elkhound
    LIVE_MMLS_DOGS_Norwegian_Lundehund: URIRef  # Norwegian Lundehund
    LIVE_MMLS_DOGS_Norwich_Terrier: URIRef  # Norwich Terrier
    LIVE_MMLS_DOGS_Nova_Scotia_Duck_Tolling_Retriever: (
        URIRef  # Nova Scotia Duck-Tolling Retriever
    )
    LIVE_MMLS_DOGS_Old_English_Bulldog: URIRef  # Old English Bulldog
    LIVE_MMLS_DOGS_Old_English_Sheepdog: URIRef  # Old English Sheepdog
    LIVE_MMLS_DOGS_Olde_English_Bulldog: URIRef  # Olde English Bulldog
    LIVE_MMLS_DOGS_Otterhound: URIRef  # Otterhound
    LIVE_MMLS_DOGS_Papillon: URIRef  # Papillon
    LIVE_MMLS_DOGS_Parson_Russell_Terrier: URIRef  # Parson Russell Terrier
    LIVE_MMLS_DOGS_Peekapoo_Pekingese_Poodle_Mix: (
        URIRef  # Peekapoo-Pekingese Poodle Mix
    )
    LIVE_MMLS_DOGS_Pekingese: URIRef  # Pekingese
    LIVE_MMLS_DOGS_Pembroke_Welsh_Corgi: URIRef  # Pembroke Welsh Corgi
    LIVE_MMLS_DOGS_Petit_Basset_Griffon_Vendéen: URIRef  # Petit Basset Griffon Vendéen
    LIVE_MMLS_DOGS_Pharaoh_Hound: URIRef  # Pharaoh Hound
    LIVE_MMLS_DOGS_Pit_Bull: URIRef  # Pit Bull
    LIVE_MMLS_DOGS_Pit_Plott_Pitbull_Plott_Hound_Mix: (
        URIRef  # Pit Plott-Pitbull Plott Hound Mix
    )
    LIVE_MMLS_DOGS_Plott_Hound: URIRef  # Plott Hound
    LIVE_MMLS_DOGS_Pointer: URIRef  # Pointer
    LIVE_MMLS_DOGS_Polish_Lowland_Sheepdog: URIRef  # Polish Lowland Sheepdog
    LIVE_MMLS_DOGS_Pomapoo_Pomeranian_Poodle_Mix: (
        URIRef  # Pomapoo-Pomeranian Poodle Mix
    )
    LIVE_MMLS_DOGS_Pomchi_Pomeranian_Chihuahua_Mix: (
        URIRef  # Pomchi-Pomeranian Chihuahua Mix
    )
    LIVE_MMLS_DOGS_Pomeranian: URIRef  # Pomeranian
    LIVE_MMLS_DOGS_Pomsky_Pomeranian_Siberian_Husky_Mix: (
        URIRef  # Pomsky-Pomeranian Siberian Husky Mix
    )
    LIVE_MMLS_DOGS_Poochon_Poodle_Bichon_Frise_Mix: (
        URIRef  # Poochon-Poodle Bichon Frise Mix
    )
    LIVE_MMLS_DOGS_Poodle: URIRef  # Poodle
    LIVE_MMLS_DOGS_Portuguese_Podengo_Pequeno: URIRef  # Portuguese Podengo Pequeno
    LIVE_MMLS_DOGS_Portuguese_Water_Dog: URIRef  # Portuguese Water Dog
    LIVE_MMLS_DOGS_Presa_Canario: URIRef  # Presa Canario
    LIVE_MMLS_DOGS_Pug: URIRef  # Pug
    LIVE_MMLS_DOGS_Pugapoo_Pug_Poodle_Mix: URIRef  # Pugapoo-Pug Poodle Mix
    LIVE_MMLS_DOGS_Puggle_Pug_Beagle_Mix: URIRef  # Puggle-Pug Beagle Mix
    LIVE_MMLS_DOGS_Puli: URIRef  # Puli
    LIVE_MMLS_DOGS_Pyrenean_Mastiff: URIRef  # Pyrenean Mastiff
    LIVE_MMLS_DOGS_Pyrenean_Shepherd: URIRef  # Pyrenean Shepherd
    LIVE_MMLS_DOGS_Rat_Terrier: URIRef  # Rat Terrier
    LIVE_MMLS_DOGS_Redbone_Coonhound: URIRef  # Redbone Coonhound
    LIVE_MMLS_DOGS_Rhodesian_Ridgeback: URIRef  # Rhodesian Ridgeback
    LIVE_MMLS_DOGS_Rottweiler: URIRef  # Rottweiler
    LIVE_MMLS_DOGS_Russell_Terrier: URIRef  # Russell Terrier
    LIVE_MMLS_DOGS_Saint_Bernard: URIRef  # Saint Bernard
    LIVE_MMLS_DOGS_Saluki: URIRef  # Saluki
    LIVE_MMLS_DOGS_Samoyed: URIRef  # Samoyed
    LIVE_MMLS_DOGS_Schipperke: URIRef  # Schipperke
    LIVE_MMLS_DOGS_Schnoodle_Schnauzer_Poodle_Mix: (
        URIRef  # Schnoodle-Schnauzer Poodle Mix
    )
    LIVE_MMLS_DOGS_Scottish_Deerhound: URIRef  # Scottish Deerhound
    LIVE_MMLS_DOGS_Scottish_Terrier: URIRef  # Scottish Terrier
    LIVE_MMLS_DOGS_Sealyham_Terrier: URIRef  # Sealyham Terrier
    LIVE_MMLS_DOGS_Shar_Pei: URIRef  # Shar Pei
    LIVE_MMLS_DOGS_Sheepadoodle_Old_English_Sheepdog_Poodle_Mix: (
        URIRef  # Sheepadoodle-Old English Sheepdog Poodle Mix
    )
    LIVE_MMLS_DOGS_Shetland_Sheepdog: URIRef  # Shetland Sheepdog
    LIVE_MMLS_DOGS_Shiba_Inu: URIRef  # Shiba Inu
    LIVE_MMLS_DOGS_Shih_Poo: URIRef  # Shih-Poo
    LIVE_MMLS_DOGS_Shih_Tzu: URIRef  # Shih Tzu
    LIVE_MMLS_DOGS_Shihpoo_Shih_Tzu_Poodle_Mix: URIRef  # Shihpoo-Shih Tzu Poodle Mix
    LIVE_MMLS_DOGS_Siberian_Husky: URIRef  # Siberian Husky
    LIVE_MMLS_DOGS_Silky_Terrier: URIRef  # Silky Terrier
    LIVE_MMLS_DOGS_Skye_Terrier: URIRef  # Skye Terrier
    LIVE_MMLS_DOGS_Sloughi_Arabian_Greyhound: URIRef  # Sloughi-Arabian Greyhound
    LIVE_MMLS_DOGS_Smooth_Fox_Terrier: URIRef  # Smooth Fox Terrier
    LIVE_MMLS_DOGS_Soft_Coated_Wheaten_Terrier: URIRef  # Soft-Coated Wheaten Terrier
    LIVE_MMLS_DOGS_South_African_Mastiff: URIRef  # South African Mastiff
    LIVE_MMLS_DOGS_Spanish_Mastiff: URIRef  # Spanish Mastiff
    LIVE_MMLS_DOGS_Spanish_Water_Dog: URIRef  # Spanish Water Dog
    LIVE_MMLS_DOGS_Spinone_Italiano: URIRef  # Spinone Italiano
    LIVE_MMLS_DOGS_Staffordshire_Bull_Terrier: URIRef  # Staffordshire Bull Terrier
    LIVE_MMLS_DOGS_Standard_Schnauzer: URIRef  # Standard Schnauzer
    LIVE_MMLS_DOGS_Sussex_Spaniel: URIRef  # Sussex Spaniel
    LIVE_MMLS_DOGS_Swedish_Vallhund: URIRef  # Swedish Vallhund
    LIVE_MMLS_DOGS_Tibetan_Mastiff: URIRef  # Tibetan Mastiff
    LIVE_MMLS_DOGS_Tibetan_Spaniel: URIRef  # Tibetan Spaniel
    LIVE_MMLS_DOGS_Tibetan_Terrier: URIRef  # Tibetan Terrier
    LIVE_MMLS_DOGS_Tosa_Japanese_Mastiff: URIRef  # Tosa-Japanese Mastiff
    LIVE_MMLS_DOGS_Toy_Fox_Terrier: URIRef  # Toy Fox Terrier
    LIVE_MMLS_DOGS_Treeing_Walker_Coonhound: URIRef  # Treeing Walker Coonhound
    LIVE_MMLS_DOGS_Utonagan_Northern_Inuit_Dog: URIRef  # Utonagan-Northern Inuit Dog
    LIVE_MMLS_DOGS_Valley_Bulldog: URIRef  # Valley Bulldog
    LIVE_MMLS_DOGS_Vizsla: URIRef  # Vizsla
    LIVE_MMLS_DOGS_Weimaraner: URIRef  # Weimaraner
    LIVE_MMLS_DOGS_Welsh_Springer_Spaniel: URIRef  # Welsh Springer Spaniel
    LIVE_MMLS_DOGS_Welsh_Terrier: URIRef  # Welsh Terrier
    LIVE_MMLS_DOGS_West_Highland_White_Terrier: URIRef  # West Highland White Terrier
    LIVE_MMLS_DOGS_Whippet: URIRef  # Whippet
    LIVE_MMLS_DOGS_Wire_Fox_Terrier: URIRef  # Wire Fox Terrier
    LIVE_MMLS_DOGS_Wirehaired_Pointing_Griffon: URIRef  # Wirehaired Pointing Griffon
    LIVE_MMLS_DOGS_Wirehaired_Vizsla: URIRef  # Wirehaired Vizsla
    LIVE_MMLS_DOGS_Xoloitzcuintli_Mexican_Hairless_Dog: (
        URIRef  # Xoloitzcuintli-Mexican Hairless Dog
    )
    LIVE_MMLS_DOGS_Yorkipoo_Yorkshire_Terrier_Poodle_Mix: (
        URIRef  # Yorkipoo-Yorkshire Terrier Poodle Mix
    )
    LIVE_MMLS_DOGS_Yorkshire_Terrier: URIRef  # Yorkshire Terrier
    LIVE_MMLS_FERR: URIRef  # Ferrets
    LIVE_MMLS_GOAT: URIRef  # Goats
    LIVE_MMLS_HORS: URIRef  # Horses
    LIVE_MMLS_MNKY: URIRef  # Monkeys
    LIVE_MMLS_PIGS: URIRef  # Pigs
    LIVE_MMLS_RDNT: URIRef  # Rodents
    LIVE_MMLS_SHEP: URIRef  # Sheep
    LIVE_REPT: URIRef  # Reptiles
    LIVE_VANI: URIRef  # Venomous animals
    LIVE_ZOOA: URIRef  # Zoo animals
    MAIL: URIRef  # Mail
    MART: URIRef  # Musical Instruments & Art
    MART_ART: URIRef  # Art
    MART_ENGR: URIRef  # Engraving
    MART_HAND: URIRef  # Handicraft products
    MART_MUEQ: URIRef  # Musical equipment
    MART_MUSI: URIRef  # Musical instruments
    MART_PNTG: URIRef  # Painting
    MLTY: URIRef  # Military, Weapons and Ammunition
    MLTY_AMUN: URIRef  # Munitions
    MLTY_MSUP: URIRef  # Military supplies
    MLTY_SPWE: URIRef  # Sporting weapons
    MLTY_WPNS: URIRef  # Weapons
    PHAR: URIRef  # Pharmaceutical, Medical And Biological
    PHAR_BIOP: URIRef  # Biological products
    PHAR_BIOP_BIOC: URIRef  # Biochemicals
    PHAR_BIOP_HEMO: URIRef  # Hemoderivatives
    PHAR_BIOP_HUBL: URIRef  # Human blood
    PHAR_BIOP_HUSR: URIRef  # Human serum
    PHAR_BIOP_LHOR: URIRef  # Live human organs
    PHAR_BIOP_SEME: URIRef  # Semen
    PHAR_BIOP_SMPL: URIRef  # Samples
    PHAR_MDCN: URIRef  # Medicines
    PHAR_MDCN_ANTB: URIRef  # Antibiotics and Vitamins
    PHAR_MDCN_VACC: URIRef  # Vaccines
    PHAR_MDCN_VETE: URIRef  # Vetenary products
    PHAR_MEDI: URIRef  # Medical
    PHAR_PHAR: URIRef  # Pharmaceutical products
    PHAR_PHAR_SUEQ: URIRef  # Surgical equipment
    PRIN: URIRef  # Printed Matter
    PRIN_ADVM: URIRef  # Advertising materials
    PRIN_BOOK: URIRef  # Books
    PRIN_DOCU: URIRef  # Documents and Tickets
    PRIN_EDUM: URIRef  # Educational materials
    PRIN_NEWS: URIRef  # Newspapers and Magazines
    PRIN_PPRP: URIRef  # Paper products
    RAWM: URIRef  # Raw materials (Construction, Metals, Wood, Minerals, Plastic)
    RAWM_BLDM: URIRef  # Building material
    RAWM_CLAY: URIRef  # Clay products
    RAWM_GLAS: URIRef  # Glass products
    RAWM_GRAN: URIRef  # Granite slabs
    RAWM_GUMS: URIRef  # Gums-Resines
    RAWM_MARB: URIRef  # Marble
    RAWM_METL: URIRef  # Metals
    RAWM_METP: URIRef  # Metal products
    RAWM_MICA: URIRef  # Mica products
    RAWM_MINE: URIRef  # Minerals
    RAWM_MIRR: URIRef  # Mirre
    RAWM_OILS: URIRef  # Oils
    RAWM_PLST: URIRef  # Plastic products
    RAWM_QRTZ: URIRef  # Quartz
    RAWM_RUBR: URIRef  # Rubber products
    RAWM_RUBR_RTYR: URIRef  # Rubber tyres
    RAWM_STNS: URIRef  # Stones
    RAWM_WOOD: URIRef  # Wood products
    SCIN: URIRef  # Scientific Instruments
    SCIN_DEEQ: URIRef  # Densist equipment
    SCIN_DIAG: URIRef  # Diagnostics equipment
    SCIN_HEAR: URIRef  # Hearing aids
    SCIN_LBEQ: URIRef  # Laboratory equipment
    SCIN_MEEQ: URIRef  # Medical equipment
    SCIN_OPTI: URIRef  # Optical instruments
    SCIN_PRCI: URIRef  # Precision instruments
    TRPH: URIRef  # Trophies
    TRPH_HTRH: URIRef  # Hunting Trophies
    TRPH_OTRH: URIRef  # Trophies (not hunting)
    TXTL: URIRef  # Textiles, Leather and Furs
    TXTL_FREW: URIRef  # Furs excluding Wear
    TXTL_FUR: URIRef  # Fur
    TXTL_FURW: URIRef  # Furs wear
    TXTL_LEXW: URIRef  # Leather excluding Wear
    TXTL_LTHR: URIRef  # Leather
    TXTL_LTWR: URIRef  # Leather wear
    TXTL_TXEW: URIRef  # Textiles excluding Wear
    TXTL_TXEW_CARP: URIRef  # Carpets and Rugs
    TXTL_TXEW_CURT: URIRef  # Curtains and Drapery
    TXTL_TXEW_FABR: URIRef  # Textile fabric
    TXTL_TXEW_FURN: URIRef  # Textile furnish
    TXTL_TXEW_HIDE: URIRef  # Hide
    TXTL_TXEW_NDLE: URIRef  # Needlework
    TXTL_TXEW_SKIN: URIRef  # Skins
    TXTL_TXEW_TRLS: URIRef  # Textile rolls
    TXTL_TXEW_YARN: URIRef  # Yarns
    TXTL_TXLW: URIRef  # Textile wear
    TXTL_TXLW_APPR: URIRef  # Wearing appareil
    TXTL_TXLW_CLTH: URIRef  # Clothing
    TXTL_TXLW_FOOT: URIRef  # Footwear
    TXTL_TXLW_GARM: URIRef  # Garments
    TXTL_TXTL: URIRef  # Textiles
    VALU: URIRef  # Valuables
    VALU_BANK: URIRef  # Bank notes and Coins
    VALU_DIAM: URIRef  # Diamonds
    VALU_GOLD: URIRef  # Gold
    VALU_JWRY: URIRef  # Jewelery
    VALU_PLAT: URIRef  # Platinum
    VALU_PMET: URIRef  # Precious metal
    VALU_PSTN: URIRef  # Precious stones
    VALU_SLVR: URIRef  # Silver
    VALU_WTCH: URIRef  # Watches
    VHCL: URIRef  # Vehicle / Machinary, Parts, Spares
    VHCL_AIRC: URIRef  # Aircraft
    VHCL_AIRC_AACC: URIRef  # Aircraft accessories
    VHCL_AIRC_AENG: URIRef  # Aicraft engines
    VHCL_AIRC_AMTR: URIRef  # Aircraft motors
    VHCL_AIRC_APRT: URIRef  # Aircraft parts
    VHCL_AIRC_ASUP: URIRef  # Aircraft supplies
    VHCL_AIRC_AWHL: URIRef  # Aircraft wheels
    VHCL_AIRC_HELI: URIRef  # Helicopter
    VHCL_AIRC_HPRT: URIRef  # Helicopter parts
    VHCL_MACH: URIRef  # Machinery and Tools
    VHCL_MACH_COIL: URIRef  # Cable coil
    VHCL_MACH_COMP: URIRef  # Comperssors
    VHCL_MACH_HRDW: URIRef  # Hardware and Equipment
    VHCL_MACH_MECH: URIRef  # Mechanic products
    VHCL_MACH_MTSP: URIRef  # Machinery supplies and Parts
    VHCL_MACH_OILD: URIRef  # Oil drilling equipment
    VHCL_MACH_PART: URIRef  # Spare parts
    VHCL_MACH_PUEQ: URIRef  # Pumping equipment
    VHCL_SHIP: URIRef  # Ships
    VHCL_SHIP_SENG: URIRef  # Engines and Turbines
    VHCL_SHIP_SMTR: URIRef  # Motor and Generator
    VHCL_SHIP_SPAR: URIRef  # Ship parts
    VHCL_SHIP_SSPA: URIRef  # Ship spares
    VHCL_SVCL: URIRef  # Surface vehicles
    VHCL_SVCL_AUTO: URIRef  # Automobiles
    VHCL_SVCL_BICY: URIRef  # Bicycles
    VHCL_SVCL_CRTA: URIRef  # Cartainer
    VHCL_SVCL_MOTO: URIRef  # Motorcycles
    VHCL_SVCL_PART: URIRef  # Automobile parts
    VHCL_SVCL_TIRE: URIRef  # Tires
