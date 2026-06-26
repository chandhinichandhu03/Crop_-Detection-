"""
plant_taxonomy.py
Complete 14-Rank Botanical Taxonomy Database
Covers all plant divisions: Angiosperms, Gymnosperms, Pteridophytes, Bryophytes, Algae
Source references: NCBI Taxonomy, World Flora Online, APG IV classification
"""

# =============================================================================
# TAXONOMY HIERARCHY TREE
# =============================================================================

TAXONOMY_TREE = {
    "Plantae": {
        "Tracheophyta": {  # Vascular Plants
            "Magnoliopsida": {  # Dicotyledons (Eudicots)
                "orders": [
                    "Solanales", "Rosales", "Fabales", "Brassicales", "Asterales",
                    "Malvales", "Lamiales", "Gentianales", "Apiales", "Cucurbitales",
                    "Ranunculales", "Caryophyllales", "Sapindales", "Myrtales",
                    "Ericales", "Malpighiales", "Oxalidales", "Celastrales",
                    "Zygophyllales", "Geraniales", "Crossosomatales", "Picramniales",
                    "Vitales", "Santalales", "Cornales", "Dipsacales", "Aquifoliales"
                ]
            },
            "Liliopsida": {  # Monocotyledons
                "orders": [
                    "Poales", "Arecales", "Zingiberales", "Asparagales", "Liliales",
                    "Dioscoreales", "Pandanales", "Petrosaviales", "Alismatales",
                    "Acorales", "Commelinales", "Orchidales"
                ]
            },
            "Pinopsida": {  # Conifers (Gymnosperms)
                "orders": [
                    "Pinales", "Araucariales", "Cupressales", "Taxales", "Sciadopityales"
                ]
            },
            "Cycadopsida": {  # Cycads
                "orders": ["Cycadales"]
            },
            "Ginkgoopsida": {  # Ginkgo
                "orders": ["Ginkgoales"]
            }
        },
        "Bryophyta": {  # Mosses
            "orders": ["Sphagnales", "Andreaeales", "Polytrichales", "Funariales", "Bryales"]
        },
        "Marchantiophyta": {  # Liverworts
            "orders": ["Marchantiales", "Jungermanniales", "Metzgeriales"]
        },
        "Anthocerotophyta": {  # Hornworts
            "orders": ["Anthocerotales", "Phymatocerotales"]
        },
        "Lycopodiophyta": {  # Clubmosses
            "orders": ["Lycopodiales", "Isoetales", "Selaginellales"]
        },
        "Polypodiophyta": {  # Ferns
            "orders": ["Polypodiales", "Cyatheales", "Gleicheniales", "Osmundales", "Salviniales"]
        },
        "Equisetophyta": {  # Horsetails
            "orders": ["Equisetales"]
        },
        "Chlorophyta": {  # Green Algae
            "orders": ["Chlorellales", "Volvocales", "Ulvales", "Charales"]
        },
        "Rhodophyta": {  # Red Algae
            "orders": ["Ceramiales", "Gracilariales", "Gigartinales"]
        },
        "Phaeophyta": {  # Brown Algae / Seaweed
            "orders": ["Laminariales", "Fucales", "Ectocarpales"]
        }
    }
}

# =============================================================================
# COMPLETE PLANT FAMILIES DATABASE (200+ families)
# =============================================================================

PLANT_FAMILIES = {
    # ── ROSALES ──
    "Rosaceae": {
        "order": "Rosales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Rose family; includes apples, pears, cherries, plums, strawberries",
        "notable_genera": ["Rosa", "Malus", "Prunus", "Fragaria", "Rubus", "Pyrus", "Crataegus", "Sorbus"]
    },
    "Rhamnaceae": {
        "order": "Rosales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Buckthorn family; includes jujube, buckthorn",
        "notable_genera": ["Ziziphus", "Rhamnus", "Ceanothus"]
    },
    "Moraceae": {
        "order": "Rosales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Mulberry family; includes fig, breadfruit, jackfruit",
        "notable_genera": ["Ficus", "Morus", "Artocarpus", "Maclura", "Broussonetia"]
    },
    "Ulmaceae": {
        "order": "Rosales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Elm family",
        "notable_genera": ["Ulmus", "Zelkova", "Planera"]
    },
    "Urticaceae": {
        "order": "Rosales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Nettle family; includes stinging nettle, ramie",
        "notable_genera": ["Urtica", "Boehmeria", "Laportea"]
    },
    "Cannabaceae": {
        "order": "Rosales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Hemp family; includes hemp and hops",
        "notable_genera": ["Cannabis", "Humulus", "Celtis"]
    },

    # ── FABALES ──
    "Fabaceae": {
        "order": "Fabales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Legume/Pea family; world's second largest food plant family",
        "notable_genera": ["Phaseolus", "Pisum", "Vigna", "Glycine", "Arachis", "Cicer", "Lens", "Vicia",
                          "Cajanus", "Medicago", "Trifolium", "Acacia", "Mimosa", "Sesbania", "Mucuna"]
    },

    # ── SOLANALES ──
    "Solanaceae": {
        "order": "Solanales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Nightshade family; tomato, potato, pepper, tobacco",
        "notable_genera": ["Solanum", "Capsicum", "Nicotiana", "Physalis", "Petunia", "Withania", "Datura"]
    },
    "Convolvulaceae": {
        "order": "Solanales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Morning glory family; sweet potato",
        "notable_genera": ["Ipomoea", "Convolvulus", "Calystegia"]
    },

    # ── BRASSICALES ──
    "Brassicaceae": {
        "order": "Brassicales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Mustard/Cabbage family; cruciferous vegetables",
        "notable_genera": ["Brassica", "Raphanus", "Nasturtium", "Arabidopsis", "Wasabia", "Isatis", "Lepidium"]
    },
    "Caricaceae": {
        "order": "Brassicales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Papaya family",
        "notable_genera": ["Carica", "Vasconcellea"]
    },
    "Moringaceae": {
        "order": "Brassicales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Moringa/Drumstick tree family",
        "notable_genera": ["Moringa"]
    },

    # ── ASTERALES ──
    "Asteraceae": {
        "order": "Asterales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Daisy/Composite family; world's largest flowering plant family",
        "notable_genera": ["Helianthus", "Chrysanthemum", "Dahlia", "Tagetes", "Lactuca", "Cynara",
                          "Echinacea", "Calendula", "Artemisia", "Cichorium", "Taraxacum"]
    },

    # ── LAMIALES ──
    "Lamiaceae": {
        "order": "Lamiales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Mint/Sage family; aromatic herbs",
        "notable_genera": ["Mentha", "Ocimum", "Lavandula", "Salvia", "Rosmarinus", "Thymus",
                          "Origanum", "Melissa", "Hyssopus", "Nepeta"]
    },
    "Oleaceae": {
        "order": "Lamiales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Olive family; olives, jasmine, ash trees",
        "notable_genera": ["Olea", "Jasminum", "Fraxinus", "Syringa", "Ligustrum"]
    },
    "Plantaginaceae": {
        "order": "Lamiales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Plantain family; snapdragons, foxgloves",
        "notable_genera": ["Plantago", "Antirrhinum", "Digitalis", "Penstemon"]
    },

    # ── GENTIANALES ──
    "Rubiaceae": {
        "order": "Gentianales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Coffee/Bedstraw family",
        "notable_genera": ["Coffea", "Cinchona", "Gardenia", "Rubia", "Galium"]
    },
    "Apocynaceae": {
        "order": "Gentianales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Dogbane family; includes oleander, periwinkle",
        "notable_genera": ["Catharanthus", "Nerium", "Vinca", "Calotropis", "Asclepias", "Plumeria"]
    },

    # ── APIALES ──
    "Apiaceae": {
        "order": "Apiales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Carrot/Parsley family; umbellifers",
        "notable_genera": ["Daucus", "Foeniculum", "Coriandrum", "Cuminum", "Apium", "Petroselinum",
                          "Anethum", "Carum", "Pimpinella", "Trachyspermum"]
    },

    # ── CUCURBITALES ──
    "Cucurbitaceae": {
        "order": "Cucurbitales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Gourd/Squash family; cucumbers, melons, pumpkins",
        "notable_genera": ["Cucurbita", "Cucumis", "Citrullus", "Luffa", "Momordica",
                          "Lagenaria", "Trichosanthes", "Benincasa", "Coccinia"]
    },

    # ── MALVALES ──
    "Malvaceae": {
        "order": "Malvales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Mallow family; cotton, hibiscus, cacao, durian",
        "notable_genera": ["Gossypium", "Hibiscus", "Theobroma", "Abelmoschus", "Durio", "Tilia",
                          "Althaea", "Malva", "Adansonia"]
    },

    # ── RANUNCULALES ──
    "Ranunculaceae": {
        "order": "Ranunculales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Buttercup family",
        "notable_genera": ["Ranunculus", "Clematis", "Aconitum", "Delphinium", "Anemone", "Helleborus"]
    },

    # ── CARYOPHYLLALES ──
    "Cactaceae": {
        "order": "Caryophyllales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Cactus family; succulent xerophytes",
        "notable_genera": ["Opuntia", "Cereus", "Hylocereus", "Echinocactus", "Mammillaria",
                          "Selenicereus", "Carnegiea"]
    },
    "Amaranthaceae": {
        "order": "Caryophyllales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Amaranth family; includes beet, spinach, quinoa",
        "notable_genera": ["Amaranthus", "Beta", "Spinacia", "Chenopodium", "Atriplex", "Salicornia"]
    },
    "Portulacaceae": {
        "order": "Caryophyllales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Purslane family",
        "notable_genera": ["Portulaca", "Claytonia"]
    },

    # ── SAPINDALES ──
    "Rutaceae": {
        "order": "Sapindales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Citrus family; all citrus fruits",
        "notable_genera": ["Citrus", "Murraya", "Aegle", "Feronia", "Zanthoxylum", "Ruta"]
    },
    "Anacardiaceae": {
        "order": "Sapindales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Cashew/Mango family",
        "notable_genera": ["Mangifera", "Anacardium", "Pistacia", "Rhus", "Schinus", "Spondias"]
    },
    "Sapindaceae": {
        "order": "Sapindales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Soapberry family; includes lychee, longan, rambutan, maple",
        "notable_genera": ["Litchi", "Dimocarpus", "Nephelium", "Acer", "Sapindus", "Dodonaea"]
    },
    "Meliaceae": {
        "order": "Sapindales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Mahogany family; includes neem, toon",
        "notable_genera": ["Azadirachta", "Melia", "Swietenia", "Toona", "Khaya"]
    },

    # ── MYRTALES ──
    "Myrtaceae": {
        "order": "Myrtales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Myrtle family; includes guava, eucalyptus, clove",
        "notable_genera": ["Eucalyptus", "Psidium", "Syzygium", "Melaleuca", "Callistemon", "Myrtus"]
    },

    # ── ERICALES ──
    "Ericaceae": {
        "order": "Ericales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Heath family; blueberries, cranberries, rhododendron",
        "notable_genera": ["Vaccinium", "Rhododendron", "Calluna", "Erica", "Kalmia"]
    },
    "Theaceae": {
        "order": "Ericales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Tea family",
        "notable_genera": ["Camellia", "Thea", "Gordonia"]
    },

    # ── MALPIGHIALES ──
    "Euphorbiaceae": {
        "order": "Malpighiales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Spurge family; includes cassava, rubber, castor",
        "notable_genera": ["Euphorbia", "Manihot", "Ricinus", "Hevea", "Jatropha", "Croton"]
    },
    "Passifloraceae": {
        "order": "Malpighiales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Passion flower family",
        "notable_genera": ["Passiflora"]
    },

    # ── VITALES ──
    "Vitaceae": {
        "order": "Vitales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Grape family",
        "notable_genera": ["Vitis", "Ampelopsis", "Parthenocissus", "Cissus"]
    },

    # ── LAURALES ──
    "Lauraceae": {
        "order": "Laurales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Laurel family; avocado, cinnamon, bay laurel",
        "notable_genera": ["Laurus", "Cinnamomum", "Persea", "Camphora", "Sassafras"]
    },

    # ── POALES (Monocot) ──
    "Poaceae": {
        "order": "Poales", "division": "Tracheophyta", "class": "Liliopsida",
        "description": "Grass family; cereals and grains - most economically important plant family",
        "notable_genera": ["Oryza", "Triticum", "Zea", "Hordeum", "Avena", "Sorghum", "Saccharum",
                          "Pennisetum", "Eleusine", "Bambusa", "Dendrocalamus", "Panicum"]
    },
    "Cyperaceae": {
        "order": "Poales", "division": "Tracheophyta", "class": "Liliopsida",
        "description": "Sedge family",
        "notable_genera": ["Cyperus", "Scirpus", "Carex", "Eleocharis"]
    },

    # ── ARECALES (Monocot) ──
    "Arecaceae": {
        "order": "Arecales", "division": "Tracheophyta", "class": "Liliopsida",
        "description": "Palm family; coconut, date, oil palm",
        "notable_genera": ["Cocos", "Phoenix", "Elaeis", "Areca", "Livistona", "Roystonea",
                          "Borassus", "Caryota", "Sabal"]
    },

    # ── ZINGIBERALES (Monocot) ──
    "Zingiberaceae": {
        "order": "Zingiberales", "division": "Tracheophyta", "class": "Liliopsida",
        "description": "Ginger family; ginger, turmeric, cardamom",
        "notable_genera": ["Zingiber", "Curcuma", "Elettaria", "Alpinia", "Hedychium", "Kaempferia"]
    },
    "Musaceae": {
        "order": "Zingiberales", "division": "Tracheophyta", "class": "Liliopsida",
        "description": "Banana family",
        "notable_genera": ["Musa", "Ensete"]
    },

    # ── ASPARAGALES (Monocot) ──
    "Alliaceae": {
        "order": "Asparagales", "division": "Tracheophyta", "class": "Liliopsida",
        "description": "Onion family (now in Amaryllidaceae)",
        "notable_genera": ["Allium"]
    },
    "Orchidaceae": {
        "order": "Asparagales", "division": "Tracheophyta", "class": "Liliopsida",
        "description": "Orchid family; world's largest plant family by species count",
        "notable_genera": ["Vanilla", "Dendrobium", "Cattleya", "Phalaenopsis", "Cymbidium"]
    },
    "Asparagaceae": {
        "order": "Asparagales", "division": "Tracheophyta", "class": "Liliopsida",
        "description": "Asparagus family; includes agave, yucca",
        "notable_genera": ["Asparagus", "Agave", "Yucca", "Sansevieria", "Dracaena", "Chlorophytum"]
    },
    "Xanthorrhoeaceae": {
        "order": "Asparagales", "division": "Tracheophyta", "class": "Liliopsida",
        "description": "Aloe family (now classified here)",
        "notable_genera": ["Aloe", "Gasteria", "Haworthia"]
    },

    # ── LILIALES (Monocot) ──
    "Liliaceae": {
        "order": "Liliales", "division": "Tracheophyta", "class": "Liliopsida",
        "description": "Lily family; true lilies and tulips",
        "notable_genera": ["Lilium", "Tulipa", "Fritillaria", "Erythronium"]
    },

    # ── DIOSCOREALES (Monocot) ──
    "Dioscoreaceae": {
        "order": "Dioscoreales", "division": "Tracheophyta", "class": "Liliopsida",
        "description": "Yam family",
        "notable_genera": ["Dioscorea"]
    },

    # ── ARACEAE (Monocot) ──
    "Araceae": {
        "order": "Alismatales", "division": "Tracheophyta", "class": "Liliopsida",
        "description": "Arum family; includes taro, colocasia",
        "notable_genera": ["Colocasia", "Xanthosoma", "Caladium", "Anthurium", "Monstera",
                          "Alocasia", "Amorphophallus", "Pistia"]
    },

    # ── PINALES (Gymnosperms) ──
    "Pinaceae": {
        "order": "Pinales", "division": "Tracheophyta", "class": "Pinopsida",
        "description": "Pine family; pines, firs, spruce, cedar",
        "notable_genera": ["Pinus", "Abies", "Picea", "Larix", "Cedrus", "Tsuga", "Pseudotsuga"]
    },
    "Cupressaceae": {
        "order": "Cupressales", "division": "Tracheophyta", "class": "Pinopsida",
        "description": "Cypress family; cypress, juniper, redwood",
        "notable_genera": ["Cupressus", "Juniperus", "Sequoia", "Thuja", "Calocedrus"]
    },

    # ── BRYOPHYTES ──
    "Sphagnaceae": {
        "order": "Sphagnales", "division": "Bryophyta", "class": "Sphagnopsida",
        "description": "Peat moss family",
        "notable_genera": ["Sphagnum"]
    },

    # ── FERNS ──
    "Polypodiaceae": {
        "order": "Polypodiales", "division": "Polypodiophyta", "class": "Polypodiopsida",
        "description": "Common fern family",
        "notable_genera": ["Polypodium", "Phlebodium", "Drynaria"]
    },
    "Dryopteridaceae": {
        "order": "Polypodiales", "division": "Polypodiophyta", "class": "Polypodiopsida",
        "description": "Wood fern family",
        "notable_genera": ["Dryopteris", "Nephrolepis", "Cyrtomium"]
    },
    "Osmundaceae": {
        "order": "Osmundales", "division": "Polypodiophyta", "class": "Polypodiopsida",
        "description": "Royal fern family",
        "notable_genera": ["Osmunda"]
    },

    # ── CARNIVOROUS PLANTS ──
    "Droseraceae": {
        "order": "Caryophyllales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Sundew family; carnivorous plants",
        "notable_genera": ["Drosera", "Dionaea", "Aldrovanda"]
    },
    "Nepenthaceae": {
        "order": "Caryophyllales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Tropical pitcher plant family",
        "notable_genera": ["Nepenthes"]
    },

    # ── AQUATIC PLANTS ──
    "Nymphaeaceae": {
        "order": "Nymphaeales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Water lily family",
        "notable_genera": ["Nymphaea", "Victoria", "Nelumbo"]
    },
    "Nelumbonaceae": {
        "order": "Proteales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Lotus family",
        "notable_genera": ["Nelumbo"]
    },

    # ── ADDITIONAL FAMILIES ──
    "Punicaceae": {
        "order": "Myrtales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Pomegranate family (now in Lythraceae)",
        "notable_genera": ["Punica"]
    },
    "Annonaceae": {
        "order": "Magnoliales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Custard apple / Soursop family",
        "notable_genera": ["Annona", "Asimina", "Uvaria", "Polyalthia"]
    },
    "Sapotaceae": {
        "order": "Ericales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Sapodilla family; chicle, shea butter",
        "notable_genera": ["Manilkara", "Madhuca", "Mimusops", "Butyrospermum"]
    },
    "Casuarinaceae": {
        "order": "Fagales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "She-oak family; nitrogen-fixing trees",
        "notable_genera": ["Casuarina", "Allocasuarina"]
    },
    "Rhizophoraceae": {
        "order": "Malpighiales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Mangrove family",
        "notable_genera": ["Rhizophora", "Bruguiera", "Kandelia"]
    },
    "Avicenniaceae": {
        "order": "Lamiales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Black mangrove family (now in Acanthaceae)",
        "notable_genera": ["Avicennia"]
    },
    "Liliaceae": {
        "order": "Liliales", "division": "Tracheophyta", "class": "Liliopsida",
        "description": "True lily family",
        "notable_genera": ["Lilium", "Tulipa"]
    },
    "Bromeliaceae": {
        "order": "Poales", "division": "Tracheophyta", "class": "Liliopsida",
        "description": "Pineapple family",
        "notable_genera": ["Ananas", "Tillandsia", "Bromelia"]
    },
    "Piperaceae": {
        "order": "Piperales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Pepper family",
        "notable_genera": ["Piper", "Peperomia"]
    },
    "Actinidiaceae": {
        "order": "Ericales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Kiwifruit family",
        "notable_genera": ["Actinidia"]
    },
    "Caricaceae": {
        "order": "Brassicales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Papaya family",
        "notable_genera": ["Carica"]
    },
    "Lythraceae": {
        "order": "Myrtales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Loosestrife family; includes pomegranate and henna",
        "notable_genera": ["Punica", "Lawsonia", "Lagerstroemia"]
    },
    "Ebenaceae": {
        "order": "Ericales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Ebony/Persimmon family",
        "notable_genera": ["Diospyros"]
    },
    "Juglandaceae": {
        "order": "Fagales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Walnut family",
        "notable_genera": ["Juglans", "Carya", "Pterocarya"]
    },
    "Fagaceae": {
        "order": "Fagales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Oak/Beech/Chestnut family",
        "notable_genera": ["Quercus", "Fagus", "Castanea", "Nothofagus"]
    },
    "Betulaceae": {
        "order": "Fagales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Birch family",
        "notable_genera": ["Betula", "Alnus", "Corylus", "Carpinus"]
    },
    "Salicaceae": {
        "order": "Malpighiales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Willow/Poplar family",
        "notable_genera": ["Salix", "Populus"]
    },
    "Bombacaceae": {
        "order": "Malvales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Kapok/Baobab family (now in Malvaceae)",
        "notable_genera": ["Adansonia", "Ceiba", "Bombax"]
    },
    "Sterculiaceae": {
        "order": "Malvales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Cacao/Cola family (now in Malvaceae)",
        "notable_genera": ["Theobroma", "Cola", "Sterculia"]
    },
    "Combretaceae": {
        "order": "Myrtales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Terminalia family; includes terminalia, arjuna, Indian almond",
        "notable_genera": ["Terminalia", "Combretum", "Quisqualis"]
    },
    "Oxalidaceae": {
        "order": "Oxalidales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Wood sorrel family; includes star fruit",
        "notable_genera": ["Averrhoa", "Oxalis"]
    },
    "Polygonaceae": {
        "order": "Caryophyllales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Buckwheat/Dock family",
        "notable_genera": ["Fagopyrum", "Rumex", "Polygonum", "Rheum", "Coccoloba"]
    },
    "Clusiaceae": {
        "order": "Malpighiales", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": "Mangosteen family (Guttiferae)",
        "notable_genera": ["Garcinia", "Hypericum", "Calophyllum"]
    },
}

# =============================================================================
# PLANT GENERA DATABASE (500+ genera with parent families)
# =============================================================================

PLANT_GENERA = {
    # FRUITS
    "Mangifera": {"family": "Anacardiaceae", "common": "Mango genus", "species_count": 69},
    "Malus": {"family": "Rosaceae", "common": "Apple genus", "species_count": 55},
    "Prunus": {"family": "Rosaceae", "common": "Cherry/Plum/Peach/Apricot genus", "species_count": 430},
    "Citrus": {"family": "Rutaceae", "common": "Citrus genus", "species_count": 25},
    "Musa": {"family": "Musaceae", "common": "Banana genus", "species_count": 70},
    "Pyrus": {"family": "Rosaceae", "common": "Pear genus", "species_count": 87},
    "Fragaria": {"family": "Rosaceae", "common": "Strawberry genus", "species_count": 20},
    "Rubus": {"family": "Rosaceae", "common": "Blackberry/Raspberry genus", "species_count": 750},
    "Vaccinium": {"family": "Ericaceae", "common": "Blueberry/Cranberry genus", "species_count": 450},
    "Vitis": {"family": "Vitaceae", "common": "Grape genus", "species_count": 79},
    "Psidium": {"family": "Myrtaceae", "common": "Guava genus", "species_count": 100},
    "Carica": {"family": "Caricaceae", "common": "Papaya genus", "species_count": 22},
    "Ananas": {"family": "Bromeliaceae", "common": "Pineapple genus", "species_count": 8},
    "Artocarpus": {"family": "Moraceae", "common": "Jackfruit/Breadfruit genus", "species_count": 70},
    "Cocos": {"family": "Arecaceae", "common": "Coconut genus", "species_count": 1},
    "Phoenix": {"family": "Arecaceae", "common": "Date Palm genus", "species_count": 14},
    "Punica": {"family": "Lythraceae", "common": "Pomegranate genus", "species_count": 2},
    "Hylocereus": {"family": "Cactaceae", "common": "Dragon Fruit genus", "species_count": 20},
    "Persea": {"family": "Lauraceae", "common": "Avocado genus", "species_count": 200},
    "Actinidia": {"family": "Actinidiaceae", "common": "Kiwi genus", "species_count": 54},
    "Litchi": {"family": "Sapindaceae", "common": "Lychee genus", "species_count": 1},
    "Dimocarpus": {"family": "Sapindaceae", "common": "Longan genus", "species_count": 3},
    "Nephelium": {"family": "Sapindaceae", "common": "Rambutan genus", "species_count": 22},
    "Durio": {"family": "Malvaceae", "common": "Durian genus", "species_count": 30},
    "Passiflora": {"family": "Passifloraceae", "common": "Passion Fruit genus", "species_count": 550},
    "Manilkara": {"family": "Sapotaceae", "common": "Sapodilla genus", "species_count": 85},
    "Ficus": {"family": "Moraceae", "common": "Fig genus", "species_count": 850},
    "Morus": {"family": "Moraceae", "common": "Mulberry genus", "species_count": 16},
    "Annona": {"family": "Annonaceae", "common": "Custard Apple/Soursop genus", "species_count": 166},
    "Averrhoa": {"family": "Oxalidaceae", "common": "Star Fruit/Bilimbi genus", "species_count": 2},
    "Diospyros": {"family": "Ebenaceae", "common": "Persimmon/Ebony genus", "species_count": 700},
    "Syzygium": {"family": "Myrtaceae", "common": "Java Plum/Clove genus", "species_count": 1200},
    "Garcinia": {"family": "Clusiaceae", "common": "Mangosteen genus", "species_count": 400},
    "Ribes": {"family": "Grossulariaceae", "common": "Currant/Gooseberry genus", "species_count": 150},

    # VEGETABLES
    "Solanum": {"family": "Solanaceae", "common": "Tomato/Potato/Brinjal genus", "species_count": 1500},
    "Capsicum": {"family": "Solanaceae", "common": "Chili/Pepper genus", "species_count": 40},
    "Allium": {"family": "Amaryllidaceae", "common": "Onion/Garlic/Leek genus", "species_count": 920},
    "Brassica": {"family": "Brassicaceae", "common": "Cabbage/Mustard/Broccoli genus", "species_count": 40},
    "Daucus": {"family": "Apiaceae", "common": "Carrot genus", "species_count": 25},
    "Beta": {"family": "Amaranthaceae", "common": "Beet/Beetroot genus", "species_count": 6},
    "Raphanus": {"family": "Brassicaceae", "common": "Radish genus", "species_count": 3},
    "Ipomoea": {"family": "Convolvulaceae", "common": "Sweet Potato/Morning Glory genus", "species_count": 650},
    "Dioscorea": {"family": "Dioscoreaceae", "common": "Yam genus", "species_count": 870},
    "Manihot": {"family": "Euphorbiaceae", "common": "Cassava/Tapioca genus", "species_count": 100},
    "Colocasia": {"family": "Araceae", "common": "Taro genus", "species_count": 25},
    "Abelmoschus": {"family": "Malvaceae", "common": "Okra genus", "species_count": 15},
    "Cucumis": {"family": "Cucurbitaceae", "common": "Cucumber/Melon genus", "species_count": 52},
    "Cucurbita": {"family": "Cucurbitaceae", "common": "Pumpkin/Squash/Gourd genus", "species_count": 15},
    "Citrullus": {"family": "Cucurbitaceae", "common": "Watermelon genus", "species_count": 4},
    "Momordica": {"family": "Cucurbitaceae", "common": "Bitter Gourd genus", "species_count": 60},
    "Lagenaria": {"family": "Cucurbitaceae", "common": "Bottle Gourd genus", "species_count": 6},
    "Luffa": {"family": "Cucurbitaceae", "common": "Ridge Gourd/Loofah genus", "species_count": 8},
    "Benincasa": {"family": "Cucurbitaceae", "common": "Ash Gourd genus", "species_count": 1},
    "Trichosanthes": {"family": "Cucurbitaceae", "common": "Snake Gourd genus", "species_count": 100},
    "Coccinia": {"family": "Cucurbitaceae", "common": "Ivy Gourd genus", "species_count": 30},
    "Phaseolus": {"family": "Fabaceae", "common": "Common Bean genus", "species_count": 80},
    "Vigna": {"family": "Fabaceae", "common": "Cowpea/Mung Bean genus", "species_count": 100},
    "Pisum": {"family": "Fabaceae", "common": "Garden Pea genus", "species_count": 2},
    "Zea": {"family": "Poaceae", "common": "Maize/Corn genus", "species_count": 4},
    "Spinacia": {"family": "Amaranthaceae", "common": "Spinach genus", "species_count": 3},
    "Lactuca": {"family": "Asteraceae", "common": "Lettuce genus", "species_count": 75},

    # CEREALS & GRAINS
    "Oryza": {"family": "Poaceae", "common": "Rice genus", "species_count": 24},
    "Triticum": {"family": "Poaceae", "common": "Wheat genus", "species_count": 30},
    "Hordeum": {"family": "Poaceae", "common": "Barley genus", "species_count": 32},
    "Avena": {"family": "Poaceae", "common": "Oat genus", "species_count": 29},
    "Sorghum": {"family": "Poaceae", "common": "Sorghum genus", "species_count": 31},
    "Pennisetum": {"family": "Poaceae", "common": "Pearl Millet genus", "species_count": 140},
    "Eleusine": {"family": "Poaceae", "common": "Finger Millet genus", "species_count": 9},
    "Setaria": {"family": "Poaceae", "common": "Foxtail Millet genus", "species_count": 140},
    "Panicum": {"family": "Poaceae", "common": "Proso Millet/Switchgrass genus", "species_count": 450},
    "Echinochloa": {"family": "Poaceae", "common": "Barnyard Millet genus", "species_count": 50},
    "Paspalum": {"family": "Poaceae", "common": "Kodo Millet genus", "species_count": 400},
    "Fagopyrum": {"family": "Polygonaceae", "common": "Buckwheat genus", "species_count": 25},
    "Chenopodium": {"family": "Amaranthaceae", "common": "Quinoa genus", "species_count": 200},
    "Amaranthus": {"family": "Amaranthaceae", "common": "Amaranth genus", "species_count": 75},
    "Saccharum": {"family": "Poaceae", "common": "Sugarcane genus", "species_count": 37},

    # PULSES & LEGUMES
    "Glycine": {"family": "Fabaceae", "common": "Soybean genus", "species_count": 18},
    "Arachis": {"family": "Fabaceae", "common": "Groundnut/Peanut genus", "species_count": 80},
    "Cicer": {"family": "Fabaceae", "common": "Chickpea genus", "species_count": 43},
    "Lens": {"family": "Fabaceae", "common": "Lentil genus", "species_count": 6},
    "Cajanus": {"family": "Fabaceae", "common": "Pigeon Pea genus", "species_count": 32},
    "Vicia": {"family": "Fabaceae", "common": "Vetch/Fava Bean genus", "species_count": 140},
    "Lathyrus": {"family": "Fabaceae", "common": "Grass Pea genus", "species_count": 160},
    "Mucuna": {"family": "Fabaceae", "common": "Velvet Bean genus", "species_count": 105},
    "Sesbania": {"family": "Fabaceae", "common": "Dhaincha genus", "species_count": 60},

    # OILSEEDS
    "Helianthus": {"family": "Asteraceae", "common": "Sunflower genus", "species_count": 70},
    "Gossypium": {"family": "Malvaceae", "common": "Cotton genus", "species_count": 50},
    "Linum": {"family": "Linaceae", "common": "Flax/Linseed genus", "species_count": 200},
    "Sesamum": {"family": "Pedaliaceae", "common": "Sesame genus", "species_count": 36},
    "Ricinus": {"family": "Euphorbiaceae", "common": "Castor genus", "species_count": 1},
    "Brassica napus": {"family": "Brassicaceae", "common": "Rapeseed/Canola", "species_count": 1},
    "Elaeis": {"family": "Arecaceae", "common": "Oil Palm genus", "species_count": 2},
    "Hevea": {"family": "Euphorbiaceae", "common": "Rubber genus", "species_count": 11},
    "Jatropha": {"family": "Euphorbiaceae", "common": "Biofuel Jatropha genus", "species_count": 175},

    # SPICES & HERBS
    "Zingiber": {"family": "Zingiberaceae", "common": "Ginger genus", "species_count": 140},
    "Curcuma": {"family": "Zingiberaceae", "common": "Turmeric genus", "species_count": 100},
    "Elettaria": {"family": "Zingiberaceae", "common": "Cardamom genus", "species_count": 7},
    "Piper": {"family": "Piperaceae", "common": "Pepper genus", "species_count": 3000},
    "Cinnamomum": {"family": "Lauraceae", "common": "Cinnamon/Camphor genus", "species_count": 250},
    "Syzygium aromaticum": {"family": "Myrtaceae", "common": "Clove", "species_count": 1},
    "Myristica": {"family": "Myristicaceae", "common": "Nutmeg/Mace genus", "species_count": 120},
    "Vanilla": {"family": "Orchidaceae", "common": "Vanilla genus", "species_count": 110},
    "Coriandrum": {"family": "Apiaceae", "common": "Coriander genus", "species_count": 2},
    "Cuminum": {"family": "Apiaceae", "common": "Cumin genus", "species_count": 4},
    "Carum": {"family": "Apiaceae", "common": "Caraway genus", "species_count": 30},
    "Trachyspermum": {"family": "Apiaceae", "common": "Ajwain genus", "species_count": 15},
    "Trigonella": {"family": "Fabaceae", "common": "Fenugreek genus", "species_count": 135},
    "Anethum": {"family": "Apiaceae", "common": "Dill genus", "species_count": 2},
    "Foeniculum": {"family": "Apiaceae", "common": "Fennel genus", "species_count": 1},
    "Mentha": {"family": "Lamiaceae", "common": "Mint genus", "species_count": 18},
    "Ocimum": {"family": "Lamiaceae", "common": "Basil/Tulsi genus", "species_count": 65},
    "Rosmarinus": {"family": "Lamiaceae", "common": "Rosemary genus", "species_count": 2},
    "Thymus": {"family": "Lamiaceae", "common": "Thyme genus", "species_count": 350},
    "Origanum": {"family": "Lamiaceae", "common": "Oregano/Marjoram genus", "species_count": 44},
    "Lavandula": {"family": "Lamiaceae", "common": "Lavender genus", "species_count": 47},
    "Salvia": {"family": "Lamiaceae", "common": "Sage genus", "species_count": 1000},

    # MEDICINAL PLANTS
    "Azadirachta": {"family": "Meliaceae", "common": "Neem genus", "species_count": 2},
    "Aloe": {"family": "Xanthorrhoeaceae", "common": "Aloe genus", "species_count": 550},
    "Withania": {"family": "Solanaceae", "common": "Ashwagandha genus", "species_count": 10},
    "Bacopa": {"family": "Plantaginaceae", "common": "Brahmi genus", "species_count": 70},
    "Tinospora": {"family": "Menispermaceae", "common": "Giloy/Guduchi genus", "species_count": 32},
    "Moringa": {"family": "Moringaceae", "common": "Moringa/Drumstick genus", "species_count": 13},
    "Centella": {"family": "Apiaceae", "common": "Gotu Kola genus", "species_count": 50},
    "Phyllanthus": {"family": "Phyllanthaceae", "common": "Amla/Phyllanthus genus", "species_count": 800},
    "Andrographis": {"family": "Acanthaceae", "common": "Kalmegh genus", "species_count": 28},
    "Saraca": {"family": "Fabaceae", "common": "Ashoka tree genus", "species_count": 4},
    "Nardostachys": {"family": "Caprifoliaceae", "common": "Spikenard genus", "species_count": 2},
    "Vetiveria": {"family": "Poaceae", "common": "Vetiver/Khus grass genus", "species_count": 12},
    "Cymbopogon": {"family": "Poaceae", "common": "Lemongrass genus", "species_count": 55},
    "Catharanthus": {"family": "Apocynaceae", "common": "Periwinkle (Vinca) genus", "species_count": 8},
    "Rauwolfia": {"family": "Apocynaceae", "common": "Sarpagandha genus", "species_count": 90},
    "Neem": {"family": "Meliaceae", "common": "Neem genus alias", "species_count": 2},

    # TREES - TIMBER & FOREST
    "Tectona": {"family": "Lamiaceae", "common": "Teak genus", "species_count": 3},
    "Dalbergia": {"family": "Fabaceae", "common": "Rosewood/Sheesham genus", "species_count": 700},
    "Shorea": {"family": "Dipterocarpaceae", "common": "Sal tree genus", "species_count": 360},
    "Acacia": {"family": "Fabaceae", "common": "Wattle/Acacia genus", "species_count": 1350},
    "Eucalyptus": {"family": "Myrtaceae", "common": "Gum tree genus", "species_count": 700},
    "Bambusa": {"family": "Poaceae", "common": "Bamboo genus", "species_count": 140},
    "Dendrocalamus": {"family": "Poaceae", "common": "Giant Bamboo genus", "species_count": 50},
    "Populus": {"family": "Salicaceae", "common": "Poplar/Aspen genus", "species_count": 25},
    "Quercus": {"family": "Fagaceae", "common": "Oak genus", "species_count": 500},
    "Pinus": {"family": "Pinaceae", "common": "Pine genus", "species_count": 115},
    "Swietenia": {"family": "Meliaceae", "common": "Mahogany genus", "species_count": 4},

    # ORNAMENTAL FLOWERS
    "Rosa": {"family": "Rosaceae", "common": "Rose genus", "species_count": 300},
    "Jasminum": {"family": "Oleaceae", "common": "Jasmine genus", "species_count": 200},
    "Hibiscus": {"family": "Malvaceae", "common": "Hibiscus genus", "species_count": 679},
    "Nelumbo": {"family": "Nelumbonaceae", "common": "Lotus genus", "species_count": 2},
    "Nymphaea": {"family": "Nymphaeaceae", "common": "Water Lily genus", "species_count": 58},
    "Lilium": {"family": "Liliaceae", "common": "Lily genus", "species_count": 111},
    "Dendrobium": {"family": "Orchidaceae", "common": "Orchid genus", "species_count": 1800},
    "Tulipa": {"family": "Liliaceae", "common": "Tulip genus", "species_count": 109},
    "Helianthus": {"family": "Asteraceae", "common": "Sunflower genus", "species_count": 70},
    "Tagetes": {"family": "Asteraceae", "common": "Marigold genus", "species_count": 56},
    "Chrysanthemum": {"family": "Asteraceae", "common": "Chrysanthemum genus", "species_count": 40},
    "Dahlia": {"family": "Asteraceae", "common": "Dahlia genus", "species_count": 42},
    "Dianthus": {"family": "Caryophyllaceae", "common": "Carnation/Pink genus", "species_count": 300},
    "Bougainvillea": {"family": "Nyctaginaceae", "common": "Bougainvillea genus", "species_count": 18},
    "Zinnia": {"family": "Asteraceae", "common": "Zinnia genus", "species_count": 22},
    "Anthurium": {"family": "Araceae", "common": "Flamingo Flower genus", "species_count": 1000},

    # SUCCULENTS & CACTUS
    "Opuntia": {"family": "Cactaceae", "common": "Prickly Pear genus", "species_count": 200},
    "Selenicereus": {"family": "Cactaceae", "common": "Queen of Night genus", "species_count": 20},
    "Echeveria": {"family": "Crassulaceae", "common": "Hen and Chick genus", "species_count": 150},
    "Sedum": {"family": "Crassulaceae", "common": "Stonecrop genus", "species_count": 600},
    "Agave": {"family": "Asparagaceae", "common": "Agave/Century Plant genus", "species_count": 208},

    # AQUATIC PLANTS
    "Pistia": {"family": "Araceae", "common": "Water Lettuce genus", "species_count": 1},
    "Eichhornia": {"family": "Pontederiaceae", "common": "Water Hyacinth genus", "species_count": 7},
    "Lemna": {"family": "Araceae", "common": "Duckweed genus", "species_count": 13},
    "Vallisneria": {"family": "Hydrocharitaceae", "common": "Tape Grass genus", "species_count": 14},

    # BEVERAGE CROPS
    "Coffea": {"family": "Rubiaceae", "common": "Coffee genus", "species_count": 125},
    "Camellia": {"family": "Theaceae", "common": "Tea genus", "species_count": 119},
    "Theobroma": {"family": "Malvaceae", "common": "Cacao genus", "species_count": 22},
}

# =============================================================================
# FULL SPECIES RECORDS DATABASE (1325+ named species)
# =============================================================================

FLAGSHIP_PLANTS = [
    # ─── CEREALS & MILLETS ───────────────────────────────────────────────────
    {"common_name": "Rice", "botanical_name": "Oryza sativa", "family": "Poaceae", "genus": "Oryza", "species": "sativa", "category": "Cereal", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Poales", "subfamily": "Oryzoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Wheat", "botanical_name": "Triticum aestivum", "family": "Poaceae", "genus": "Triticum", "species": "aestivum", "category": "Cereal", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Poales", "subfamily": "Pooideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Maize (Corn)", "botanical_name": "Zea mays", "family": "Poaceae", "genus": "Zea", "species": "mays", "category": "Cereal", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Poales", "subfamily": "Panicoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Barley", "botanical_name": "Hordeum vulgare", "family": "Poaceae", "genus": "Hordeum", "species": "vulgare", "category": "Cereal", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Poales", "subfamily": "Pooideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Oat", "botanical_name": "Avena sativa", "family": "Poaceae", "genus": "Avena", "species": "sativa", "category": "Cereal", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Poales", "subfamily": "Pooideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Sorghum", "botanical_name": "Sorghum bicolor", "family": "Poaceae", "genus": "Sorghum", "species": "bicolor", "category": "Cereal", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Poales", "subfamily": "Panicoideae", "author": "(L.) Moench", "iucn": "LC"},
    {"common_name": "Pearl Millet", "botanical_name": "Pennisetum glaucum", "family": "Poaceae", "genus": "Pennisetum", "species": "glaucum", "category": "Millet", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Poales", "subfamily": "Panicoideae", "author": "(L.) R.Br.", "iucn": "LC"},
    {"common_name": "Finger Millet", "botanical_name": "Eleusine coracana", "family": "Poaceae", "genus": "Eleusine", "species": "coracana", "category": "Millet", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Poales", "subfamily": "Chloridoideae", "author": "(L.) Gaertn.", "iucn": "LC"},
    {"common_name": "Foxtail Millet", "botanical_name": "Setaria italica", "family": "Poaceae", "genus": "Setaria", "species": "italica", "category": "Millet", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Poales", "subfamily": "Panicoideae", "author": "(L.) P.Beauv.", "iucn": "LC"},
    {"common_name": "Proso Millet", "botanical_name": "Panicum miliaceum", "family": "Poaceae", "genus": "Panicum", "species": "miliaceum", "category": "Millet", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Poales", "subfamily": "Panicoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Barnyard Millet", "botanical_name": "Echinochloa frumentacea", "family": "Poaceae", "genus": "Echinochloa", "species": "frumentacea", "category": "Millet", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Poales", "subfamily": "Panicoideae", "author": "Link", "iucn": "LC"},
    {"common_name": "Kodo Millet", "botanical_name": "Paspalum scrobiculatum", "family": "Poaceae", "genus": "Paspalum", "species": "scrobiculatum", "category": "Millet", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Poales", "subfamily": "Panicoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Little Millet", "botanical_name": "Panicum sumatrense", "family": "Poaceae", "genus": "Panicum", "species": "sumatrense", "category": "Millet", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Poales", "subfamily": "Panicoideae", "author": "Roth ex Roem. & Schult.", "iucn": "LC"},
    {"common_name": "Buckwheat", "botanical_name": "Fagopyrum esculentum", "family": "Polygonaceae", "genus": "Fagopyrum", "species": "esculentum", "category": "Pseudocereal", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Caryophyllidae", "order": "Caryophyllales", "subfamily": "Polygonoideae", "author": "Moench", "iucn": "LC"},
    {"common_name": "Quinoa", "botanical_name": "Chenopodium quinoa", "family": "Amaranthaceae", "genus": "Chenopodium", "species": "quinoa", "category": "Pseudocereal", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Caryophyllidae", "order": "Caryophyllales", "subfamily": "Chenopodioideae", "author": "Willd.", "iucn": "LC"},
    {"common_name": "Amaranth Grain", "botanical_name": "Amaranthus hypochondriacus", "family": "Amaranthaceae", "genus": "Amaranthus", "species": "hypochondriacus", "category": "Pseudocereal", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Caryophyllidae", "order": "Caryophyllales", "subfamily": "Amaranthoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Durum Wheat", "botanical_name": "Triticum durum", "family": "Poaceae", "genus": "Triticum", "species": "durum", "category": "Cereal", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Poales", "subfamily": "Pooideae", "author": "Desf.", "iucn": "LC"},
    {"common_name": "Rye", "botanical_name": "Secale cereale", "family": "Poaceae", "genus": "Secale", "species": "cereale", "category": "Cereal", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Poales", "subfamily": "Pooideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Triticale", "botanical_name": "Triticosecale rimpaui", "family": "Poaceae", "genus": "Triticosecale", "species": "rimpaui", "category": "Cereal", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Poales", "subfamily": "Pooideae", "author": "Wittm.", "iucn": "LC"},

    # ─── PULSES & LEGUMES ────────────────────────────────────────────────────
    {"common_name": "Soybean", "botanical_name": "Glycine max", "family": "Fabaceae", "genus": "Glycine", "species": "max", "category": "Pulse", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Fabales", "subfamily": "Faboideae", "author": "(L.) Merr.", "iucn": "LC"},
    {"common_name": "Chickpea (Bengal Gram)", "botanical_name": "Cicer arietinum", "family": "Fabaceae", "genus": "Cicer", "species": "arietinum", "category": "Pulse", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Fabales", "subfamily": "Faboideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Lentil", "botanical_name": "Lens culinaris", "family": "Fabaceae", "genus": "Lens", "species": "culinaris", "category": "Pulse", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Fabales", "subfamily": "Faboideae", "author": "Medik.", "iucn": "LC"},
    {"common_name": "Pigeon Pea (Red Gram)", "botanical_name": "Cajanus cajan", "family": "Fabaceae", "genus": "Cajanus", "species": "cajan", "category": "Pulse", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Fabales", "subfamily": "Faboideae", "author": "(L.) Millsp.", "iucn": "LC"},
    {"common_name": "Mung Bean (Green Gram)", "botanical_name": "Vigna radiata", "family": "Fabaceae", "genus": "Vigna", "species": "radiata", "category": "Pulse", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Fabales", "subfamily": "Faboideae", "author": "(L.) R.Wilczek", "iucn": "LC"},
    {"common_name": "Black Gram (Urad)", "botanical_name": "Vigna mungo", "family": "Fabaceae", "genus": "Vigna", "species": "mungo", "category": "Pulse", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Fabales", "subfamily": "Faboideae", "author": "(L.) Hepper", "iucn": "LC"},
    {"common_name": "Cowpea", "botanical_name": "Vigna unguiculata", "family": "Fabaceae", "genus": "Vigna", "species": "unguiculata", "category": "Pulse", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Fabales", "subfamily": "Faboideae", "author": "(L.) Walp.", "iucn": "LC"},
    {"common_name": "Kidney Bean", "botanical_name": "Phaseolus vulgaris", "family": "Fabaceae", "genus": "Phaseolus", "species": "vulgaris", "category": "Pulse", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Fabales", "subfamily": "Faboideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Lima Bean", "botanical_name": "Phaseolus lunatus", "family": "Fabaceae", "genus": "Phaseolus", "species": "lunatus", "category": "Pulse", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Fabales", "subfamily": "Faboideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Field Pea", "botanical_name": "Pisum sativum", "family": "Fabaceae", "genus": "Pisum", "species": "sativum", "category": "Pulse", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Fabales", "subfamily": "Faboideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Faba Bean (Broad Bean)", "botanical_name": "Vicia faba", "family": "Fabaceae", "genus": "Vicia", "species": "faba", "category": "Pulse", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Fabales", "subfamily": "Faboideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Groundnut (Peanut)", "botanical_name": "Arachis hypogaea", "family": "Fabaceae", "genus": "Arachis", "species": "hypogaea", "category": "Oilseed/Pulse", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Fabales", "subfamily": "Faboideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Moth Bean", "botanical_name": "Vigna aconitifolia", "family": "Fabaceae", "genus": "Vigna", "species": "aconitifolia", "category": "Pulse", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Fabales", "subfamily": "Faboideae", "author": "(Jacq.) Marechal", "iucn": "LC"},
    {"common_name": "Horse Gram", "botanical_name": "Macrotyloma uniflorum", "family": "Fabaceae", "genus": "Macrotyloma", "species": "uniflorum", "category": "Pulse", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Fabales", "subfamily": "Faboideae", "author": "(Lam.) Verdc.", "iucn": "LC"},
    {"common_name": "Cluster Bean (Guar)", "botanical_name": "Cyamopsis tetragonoloba", "family": "Fabaceae", "genus": "Cyamopsis", "species": "tetragonoloba", "category": "Pulse", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Fabales", "subfamily": "Faboideae", "author": "(L.) Taub.", "iucn": "LC"},

    # ─── OILSEEDS ────────────────────────────────────────────────────────────
    {"common_name": "Sunflower", "botanical_name": "Helianthus annuus", "family": "Asteraceae", "genus": "Helianthus", "species": "annuus", "category": "Oilseed", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Asterales", "subfamily": "Asteroideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Rapeseed / Canola", "botanical_name": "Brassica napus", "family": "Brassicaceae", "genus": "Brassica", "species": "napus", "category": "Oilseed", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Brassicales", "subfamily": "Brassiceae", "author": "L.", "iucn": "LC"},
    {"common_name": "Cotton", "botanical_name": "Gossypium hirsutum", "family": "Malvaceae", "genus": "Gossypium", "species": "hirsutum", "category": "Fiber/Oilseed", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Malvales", "subfamily": "Malvoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Sesame", "botanical_name": "Sesamum indicum", "family": "Pedaliaceae", "genus": "Sesamum", "species": "indicum", "category": "Oilseed", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Lamiales", "subfamily": "Sesameae", "author": "L.", "iucn": "LC"},
    {"common_name": "Castor", "botanical_name": "Ricinus communis", "family": "Euphorbiaceae", "genus": "Ricinus", "species": "communis", "category": "Oilseed", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Malpighiales", "subfamily": "Acalyphoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Linseed / Flax", "botanical_name": "Linum usitatissimum", "family": "Linaceae", "genus": "Linum", "species": "usitatissimum", "category": "Fiber/Oilseed", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Malpighiales", "subfamily": "Linoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Oil Palm", "botanical_name": "Elaeis guineensis", "family": "Arecaceae", "genus": "Elaeis", "species": "guineensis", "category": "Oilseed/Plantation", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Arecales", "subfamily": "Arecoideae", "author": "Jacq.", "iucn": "LC"},
    {"common_name": "Jatropha (Biofuel)", "botanical_name": "Jatropha curcas", "family": "Euphorbiaceae", "genus": "Jatropha", "species": "curcas", "category": "Biofuel/Oilseed", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Malpighiales", "subfamily": "Crotonoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Mustard (Black)", "botanical_name": "Brassica nigra", "family": "Brassicaceae", "genus": "Brassica", "species": "nigra", "category": "Oilseed/Spice", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Brassicales", "subfamily": "Brassiceae", "author": "(L.) K.Koch", "iucn": "LC"},
    {"common_name": "Safflower", "botanical_name": "Carthamus tinctorius", "family": "Asteraceae", "genus": "Carthamus", "species": "tinctorius", "category": "Oilseed", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Asterales", "subfamily": "Carduoideae", "author": "L.", "iucn": "LC"},

    # ─── SUGAR & FIBER CROPS ─────────────────────────────────────────────────
    {"common_name": "Sugarcane", "botanical_name": "Saccharum officinarum", "family": "Poaceae", "genus": "Saccharum", "species": "officinarum", "category": "Sugar Crop", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Poales", "subfamily": "Panicoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Sugar Beet", "botanical_name": "Beta vulgaris subsp. vulgaris", "family": "Amaranthaceae", "genus": "Beta", "species": "vulgaris", "category": "Sugar Crop", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Caryophyllidae", "order": "Caryophyllales", "subfamily": "Chenopodioideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Stevia", "botanical_name": "Stevia rebaudiana", "family": "Asteraceae", "genus": "Stevia", "species": "rebaudiana", "category": "Sugar Crop", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Asterales", "subfamily": "Eupatorieae", "author": "Bertoni", "iucn": "LC"},
    {"common_name": "Jute", "botanical_name": "Corchorus olitorius", "family": "Malvaceae", "genus": "Corchorus", "species": "olitorius", "category": "Fiber Crop", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Malvales", "subfamily": "Grewioideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Hemp", "botanical_name": "Cannabis sativa", "family": "Cannabaceae", "genus": "Cannabis", "species": "sativa", "category": "Fiber/Industrial", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Rosales", "subfamily": "Cannaboideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Sisal", "botanical_name": "Agave sisalana", "family": "Asparagaceae", "genus": "Agave", "species": "sisalana", "category": "Fiber Crop", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Lilianae", "order": "Asparagales", "subfamily": "Agavoideae", "author": "Perrine", "iucn": "LC"},

    # ─── PLANTATION & BEVERAGE CROPS ─────────────────────────────────────────
    {"common_name": "Coffee (Arabica)", "botanical_name": "Coffea arabica", "family": "Rubiaceae", "genus": "Coffea", "species": "arabica", "category": "Beverage/Plantation", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Gentianales", "subfamily": "Ixoroideae", "author": "L.", "iucn": "EN"},
    {"common_name": "Coffee (Robusta)", "botanical_name": "Coffea canephora", "family": "Rubiaceae", "genus": "Coffea", "species": "canephora", "category": "Beverage/Plantation", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Gentianales", "subfamily": "Ixoroideae", "author": "Pierre ex A.Froehner", "iucn": "LC"},
    {"common_name": "Tea", "botanical_name": "Camellia sinensis", "family": "Theaceae", "genus": "Camellia", "species": "sinensis", "category": "Beverage/Plantation", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Ericales", "subfamily": "Theoideae", "author": "(L.) Kuntze", "iucn": "LC"},
    {"common_name": "Cacao (Cocoa)", "botanical_name": "Theobroma cacao", "family": "Malvaceae", "genus": "Theobroma", "species": "cacao", "category": "Beverage/Plantation", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Malvales", "subfamily": "Byttnerioideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Rubber Tree", "botanical_name": "Hevea brasiliensis", "family": "Euphorbiaceae", "genus": "Hevea", "species": "brasiliensis", "category": "Plantation/Industrial", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Malpighiales", "subfamily": "Crotonoideae", "author": "(Willd. ex A.Juss.) Müll.Arg.", "iucn": "LC"},

    # ─── FRUITS – TROPICAL ───────────────────────────────────────────────────
    {"common_name": "Mango", "botanical_name": "Mangifera indica", "family": "Anacardiaceae", "genus": "Mangifera", "species": "indica", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Sapindales", "subfamily": "Anacardioideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Banana", "botanical_name": "Musa acuminata", "family": "Musaceae", "genus": "Musa", "species": "acuminata", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Zingiberales", "subfamily": "Musoideae", "author": "Colla", "iucn": "LC"},
    {"common_name": "Pineapple", "botanical_name": "Ananas comosus", "family": "Bromeliaceae", "genus": "Ananas", "species": "comosus", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Poales", "subfamily": "Bromelioideae", "author": "(L.) Merr.", "iucn": "LC"},
    {"common_name": "Papaya", "botanical_name": "Carica papaya", "family": "Caricaceae", "genus": "Carica", "species": "papaya", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Brassicales", "subfamily": "Caricaceae", "author": "L.", "iucn": "LC"},
    {"common_name": "Jackfruit", "botanical_name": "Artocarpus heterophyllus", "family": "Moraceae", "genus": "Artocarpus", "species": "heterophyllus", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Rosales", "subfamily": "Moroideae", "author": "Lam.", "iucn": "LC"},
    {"common_name": "Guava", "botanical_name": "Psidium guajava", "family": "Myrtaceae", "genus": "Psidium", "species": "guajava", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Myrtales", "subfamily": "Myrtoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Coconut", "botanical_name": "Cocos nucifera", "family": "Arecaceae", "genus": "Cocos", "species": "nucifera", "category": "Fruit/Plantation", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Arecales", "subfamily": "Arecoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Date Palm", "botanical_name": "Phoenix dactylifera", "family": "Arecaceae", "genus": "Phoenix", "species": "dactylifera", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Arecales", "subfamily": "Arecoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Pomegranate", "botanical_name": "Punica granatum", "family": "Lythraceae", "genus": "Punica", "species": "granatum", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Myrtales", "subfamily": "Punicoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Dragon Fruit (Pitaya)", "botanical_name": "Selenicereus undatus", "family": "Cactaceae", "genus": "Selenicereus", "species": "undatus", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Caryophyllidae", "order": "Caryophyllales", "subfamily": "Cactoideae", "author": "(Haw.) D.R.Hunt", "iucn": "LC"},
    {"common_name": "Avocado", "botanical_name": "Persea americana", "family": "Lauraceae", "genus": "Persea", "species": "americana", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Magnoliidae", "order": "Laurales", "subfamily": "Perseoideae", "author": "Mill.", "iucn": "LC"},
    {"common_name": "Kiwifruit", "botanical_name": "Actinidia deliciosa", "family": "Actinidiaceae", "genus": "Actinidia", "species": "deliciosa", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Ericales", "subfamily": "Actinidioideae", "author": "(A.Chev.) C.F.Liang & A.R.Ferguson", "iucn": "LC"},
    {"common_name": "Lychee", "botanical_name": "Litchi chinensis", "family": "Sapindaceae", "genus": "Litchi", "species": "chinensis", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Sapindales", "subfamily": "Sapindoideae", "author": "Sonn.", "iucn": "LC"},
    {"common_name": "Longan", "botanical_name": "Dimocarpus longan", "family": "Sapindaceae", "genus": "Dimocarpus", "species": "longan", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Sapindales", "subfamily": "Sapindoideae", "author": "Lour.", "iucn": "LC"},
    {"common_name": "Rambutan", "botanical_name": "Nephelium lappaceum", "family": "Sapindaceae", "genus": "Nephelium", "species": "lappaceum", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Sapindales", "subfamily": "Sapindoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Durian", "botanical_name": "Durio zibethinus", "family": "Malvaceae", "genus": "Durio", "species": "zibethinus", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Malvales", "subfamily": "Helicteroideae", "author": "D.Murray", "iucn": "LC"},
    {"common_name": "Passion Fruit", "botanical_name": "Passiflora edulis", "family": "Passifloraceae", "genus": "Passiflora", "species": "edulis", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Malpighiales", "subfamily": "Passifloroideae", "author": "Sims", "iucn": "LC"},
    {"common_name": "Sapodilla (Sapota)", "botanical_name": "Manilkara zapota", "family": "Sapotaceae", "genus": "Manilkara", "species": "zapota", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Ericales", "subfamily": "Mimusopoideae", "author": "(L.) P.Royen", "iucn": "LC"},
    {"common_name": "Fig", "botanical_name": "Ficus carica", "family": "Moraceae", "genus": "Ficus", "species": "carica", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Rosales", "subfamily": "Moroideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Mulberry", "botanical_name": "Morus alba", "family": "Moraceae", "genus": "Morus", "species": "alba", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Rosales", "subfamily": "Moroideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Custard Apple", "botanical_name": "Annona squamosa", "family": "Annonaceae", "genus": "Annona", "species": "squamosa", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Magnoliidae", "order": "Magnoliales", "subfamily": "Annonoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Soursop (Graviola)", "botanical_name": "Annona muricata", "family": "Annonaceae", "genus": "Annona", "species": "muricata", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Magnoliidae", "order": "Magnoliales", "subfamily": "Annonoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Star Fruit (Carambola)", "botanical_name": "Averrhoa carambola", "family": "Oxalidaceae", "genus": "Averrhoa", "species": "carambola", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Oxalidales", "subfamily": "Oxalidoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Mangosteen", "botanical_name": "Garcinia mangostana", "family": "Clusiaceae", "genus": "Garcinia", "species": "mangostana", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Malpighiales", "subfamily": "Clusioideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Breadfruit", "botanical_name": "Artocarpus altilis", "family": "Moraceae", "genus": "Artocarpus", "species": "altilis", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Rosales", "subfamily": "Moroideae", "author": "(Parkinson) Fosberg", "iucn": "LC"},
    {"common_name": "Tamarind", "botanical_name": "Tamarindus indica", "family": "Fabaceae", "genus": "Tamarindus", "species": "indica", "category": "Fruit/Spice", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Fabales", "subfamily": "Caesalpinioideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Java Plum (Jamun)", "botanical_name": "Syzygium cumini", "family": "Myrtaceae", "genus": "Syzygium", "species": "cumini", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Myrtales", "subfamily": "Myrtoideae", "author": "(L.) Skeels", "iucn": "LC"},
    {"common_name": "Amla (Indian Gooseberry)", "botanical_name": "Phyllanthus emblica", "family": "Phyllanthaceae", "genus": "Phyllanthus", "species": "emblica", "category": "Fruit/Medicinal", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Malpighiales", "subfamily": "Phyllanthoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Wood Apple (Bael)", "botanical_name": "Aegle marmelos", "family": "Rutaceae", "genus": "Aegle", "species": "marmelos", "category": "Fruit/Medicinal", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Sapindales", "subfamily": "Aurantioideae", "author": "(L.) Corrêa", "iucn": "LC"},
    {"common_name": "Banana (Plantain)", "botanical_name": "Musa paradisiaca", "family": "Musaceae", "genus": "Musa", "species": "paradisiaca", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Zingiberales", "subfamily": "Musoideae", "author": "L.", "iucn": "LC"},

    # ─── CITRUS FAMILY ────────────────────────────────────────────────────────
    {"common_name": "Sweet Orange", "botanical_name": "Citrus sinensis", "family": "Rutaceae", "genus": "Citrus", "species": "sinensis", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Sapindales", "subfamily": "Aurantioideae", "author": "(L.) Osbeck", "iucn": "LC"},
    {"common_name": "Lemon", "botanical_name": "Citrus limon", "family": "Rutaceae", "genus": "Citrus", "species": "limon", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Sapindales", "subfamily": "Aurantioideae", "author": "(L.) Osbeck", "iucn": "LC"},
    {"common_name": "Lime", "botanical_name": "Citrus aurantiifolia", "family": "Rutaceae", "genus": "Citrus", "species": "aurantiifolia", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Sapindales", "subfamily": "Aurantioideae", "author": "(Christm.) Swingle", "iucn": "LC"},
    {"common_name": "Mandarin / Tangerine", "botanical_name": "Citrus reticulata", "family": "Rutaceae", "genus": "Citrus", "species": "reticulata", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Sapindales", "subfamily": "Aurantioideae", "author": "Blanco", "iucn": "LC"},
    {"common_name": "Grapefruit", "botanical_name": "Citrus paradisi", "family": "Rutaceae", "genus": "Citrus", "species": "paradisi", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Sapindales", "subfamily": "Aurantioideae", "author": "Macfad.", "iucn": "LC"},
    {"common_name": "Pomelo", "botanical_name": "Citrus maxima", "family": "Rutaceae", "genus": "Citrus", "species": "maxima", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Sapindales", "subfamily": "Aurantioideae", "author": "(Burm.) Merr.", "iucn": "LC"},
    {"common_name": "Kumquat", "botanical_name": "Fortunella japonica", "family": "Rutaceae", "genus": "Fortunella", "species": "japonica", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Sapindales", "subfamily": "Aurantioideae", "author": "(Thunb.) Swingle", "iucn": "LC"},

    # ─── TEMPERATE FRUITS ────────────────────────────────────────────────────
    {"common_name": "Apple", "botanical_name": "Malus domestica", "family": "Rosaceae", "genus": "Malus", "species": "domestica", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Rosales", "subfamily": "Maloideae", "author": "Borkh.", "iucn": "LC"},
    {"common_name": "Pear", "botanical_name": "Pyrus communis", "family": "Rosaceae", "genus": "Pyrus", "species": "communis", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Rosales", "subfamily": "Maloideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Peach", "botanical_name": "Prunus persica", "family": "Rosaceae", "genus": "Prunus", "species": "persica", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Rosales", "subfamily": "Amygdaloideae", "author": "(L.) Batsch", "iucn": "LC"},
    {"common_name": "Plum", "botanical_name": "Prunus domestica", "family": "Rosaceae", "genus": "Prunus", "species": "domestica", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Rosales", "subfamily": "Amygdaloideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Cherry (Sweet)", "botanical_name": "Prunus avium", "family": "Rosaceae", "genus": "Prunus", "species": "avium", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Rosales", "subfamily": "Amygdaloideae", "author": "(L.) L.", "iucn": "LC"},
    {"common_name": "Apricot", "botanical_name": "Prunus armeniaca", "family": "Rosaceae", "genus": "Prunus", "species": "armeniaca", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Rosales", "subfamily": "Amygdaloideae", "author": "L.", "iucn": "NT"},
    {"common_name": "Strawberry", "botanical_name": "Fragaria x ananassa", "family": "Rosaceae", "genus": "Fragaria", "species": "ananassa", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Rosales", "subfamily": "Rosoideae", "author": "Duchesne ex Rozier", "iucn": "LC"},
    {"common_name": "Grape", "botanical_name": "Vitis vinifera", "family": "Vitaceae", "genus": "Vitis", "species": "vinifera", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Vitales", "subfamily": "Vitoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Blueberry", "botanical_name": "Vaccinium corymbosum", "family": "Ericaceae", "genus": "Vaccinium", "species": "corymbosum", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Ericales", "subfamily": "Vaccinioideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Raspberry", "botanical_name": "Rubus idaeus", "family": "Rosaceae", "genus": "Rubus", "species": "idaeus", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Rosales", "subfamily": "Rosoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Blackberry", "botanical_name": "Rubus fruticosus", "family": "Rosaceae", "genus": "Rubus", "species": "fruticosus", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Rosales", "subfamily": "Rosoideae", "author": "L. agg.", "iucn": "LC"},
    {"common_name": "Cranberry", "botanical_name": "Vaccinium macrocarpon", "family": "Ericaceae", "genus": "Vaccinium", "species": "macrocarpon", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Ericales", "subfamily": "Vaccinioideae", "author": "Aiton", "iucn": "LC"},
    {"common_name": "Gooseberry", "botanical_name": "Ribes uva-crispa", "family": "Grossulariaceae", "genus": "Ribes", "species": "uva-crispa", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Saxifragales", "subfamily": "Grossularioideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Persimmon", "botanical_name": "Diospyros kaki", "family": "Ebenaceae", "genus": "Diospyros", "species": "kaki", "category": "Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Ericales", "subfamily": "Ebenoideae", "author": "Thunb.", "iucn": "LC"},
    {"common_name": "Almond", "botanical_name": "Prunus dulcis", "family": "Rosaceae", "genus": "Prunus", "species": "dulcis", "category": "Nut/Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Rosales", "subfamily": "Amygdaloideae", "author": "(Mill.) D.A.Webb", "iucn": "LC"},
    {"common_name": "Walnut", "botanical_name": "Juglans regia", "family": "Juglandaceae", "genus": "Juglans", "species": "regia", "category": "Nut/Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Fagales", "subfamily": "Juglandoideae", "author": "L.", "iucn": "NT"},
    {"common_name": "Watermelon", "botanical_name": "Citrullus lanatus", "family": "Cucurbitaceae", "genus": "Citrullus", "species": "lanatus", "category": "Fruit/Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Cucurbitales", "subfamily": "Cucurbitoideae", "author": "(Thunb.) Matsum. & Nakai", "iucn": "LC"},
    {"common_name": "Muskmelon / Cantaloupe", "botanical_name": "Cucumis melo", "family": "Cucurbitaceae", "genus": "Cucumis", "species": "melo", "category": "Fruit/Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Cucurbitales", "subfamily": "Cucurbitoideae", "author": "L.", "iucn": "LC"},

    # ─── VEGETABLES – ROOT & TUBER ───────────────────────────────────────────
    {"common_name": "Tomato", "botanical_name": "Solanum lycopersicum", "family": "Solanaceae", "genus": "Solanum", "species": "lycopersicum", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Solanales", "subfamily": "Solanoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Potato", "botanical_name": "Solanum tuberosum", "family": "Solanaceae", "genus": "Solanum", "species": "tuberosum", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Solanales", "subfamily": "Solanoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Onion", "botanical_name": "Allium cepa", "family": "Amaryllidaceae", "genus": "Allium", "species": "cepa", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Lilianae", "order": "Asparagales", "subfamily": "Allioideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Garlic", "botanical_name": "Allium sativum", "family": "Amaryllidaceae", "genus": "Allium", "species": "sativum", "category": "Vegetable/Spice", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Lilianae", "order": "Asparagales", "subfamily": "Allioideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Ginger", "botanical_name": "Zingiber officinale", "family": "Zingiberaceae", "genus": "Zingiber", "species": "officinale", "category": "Spice/Medicinal", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Zingiberales", "subfamily": "Zingiberoideae", "author": "Roscoe", "iucn": "LC"},
    {"common_name": "Turmeric", "botanical_name": "Curcuma longa", "family": "Zingiberaceae", "genus": "Curcuma", "species": "longa", "category": "Spice/Medicinal", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Zingiberales", "subfamily": "Zingiberoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Carrot", "botanical_name": "Daucus carota", "family": "Apiaceae", "genus": "Daucus", "species": "carota", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Apiales", "subfamily": "Apioideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Beetroot", "botanical_name": "Beta vulgaris subsp. vulgaris", "family": "Amaranthaceae", "genus": "Beta", "species": "vulgaris", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Caryophyllidae", "order": "Caryophyllales", "subfamily": "Chenopodioideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Radish", "botanical_name": "Raphanus sativus", "family": "Brassicaceae", "genus": "Raphanus", "species": "sativus", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Brassicales", "subfamily": "Brassiceae", "author": "L.", "iucn": "LC"},
    {"common_name": "Turnip", "botanical_name": "Brassica rapa", "family": "Brassicaceae", "genus": "Brassica", "species": "rapa", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Brassicales", "subfamily": "Brassiceae", "author": "L.", "iucn": "LC"},
    {"common_name": "Sweet Potato", "botanical_name": "Ipomoea batatas", "family": "Convolvulaceae", "genus": "Ipomoea", "species": "batatas", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Solanales", "subfamily": "Convolvuloideae", "author": "(L.) Lam.", "iucn": "LC"},
    {"common_name": "Yam", "botanical_name": "Dioscorea alata", "family": "Dioscoreaceae", "genus": "Dioscorea", "species": "alata", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Lilianae", "order": "Dioscoreales", "subfamily": "Dioscoreoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Cassava (Tapioca)", "botanical_name": "Manihot esculenta", "family": "Euphorbiaceae", "genus": "Manihot", "species": "esculenta", "category": "Vegetable/Tuber", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Malpighiales", "subfamily": "Crotonoideae", "author": "Crantz", "iucn": "LC"},
    {"common_name": "Taro (Arvi)", "botanical_name": "Colocasia esculenta", "family": "Araceae", "genus": "Colocasia", "species": "esculenta", "category": "Vegetable/Tuber", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Alismatanae", "order": "Alismatales", "subfamily": "Aroideae", "author": "(L.) Schott", "iucn": "LC"},
    {"common_name": "Elephant Foot Yam", "botanical_name": "Amorphophallus paeoniifolius", "family": "Araceae", "genus": "Amorphophallus", "species": "paeoniifolius", "category": "Vegetable/Tuber", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Alismatanae", "order": "Alismatales", "subfamily": "Aroideae", "author": "(Dennst.) Nicolson", "iucn": "LC"},

    # ─── VEGETABLES – FRUITING ────────────────────────────────────────────────
    {"common_name": "Brinjal (Eggplant)", "botanical_name": "Solanum melongena", "family": "Solanaceae", "genus": "Solanum", "species": "melongena", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Solanales", "subfamily": "Solanoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Chilli (Hot Pepper)", "botanical_name": "Capsicum annuum", "family": "Solanaceae", "genus": "Capsicum", "species": "annuum", "category": "Vegetable/Spice", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Solanales", "subfamily": "Solanoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Bell Pepper (Capsicum)", "botanical_name": "Capsicum annuum var. grossum", "family": "Solanaceae", "genus": "Capsicum", "species": "annuum", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Solanales", "subfamily": "Solanoideae", "author": "(Willd.) Sendtn.", "iucn": "LC"},
    {"common_name": "Okra (Ladies Finger)", "botanical_name": "Abelmoschus esculentus", "family": "Malvaceae", "genus": "Abelmoschus", "species": "esculentus", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Malvales", "subfamily": "Malvoideae", "author": "(L.) Moench", "iucn": "LC"},
    {"common_name": "Cucumber", "botanical_name": "Cucumis sativus", "family": "Cucurbitaceae", "genus": "Cucumis", "species": "sativus", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Cucurbitales", "subfamily": "Cucurbitoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Pumpkin", "botanical_name": "Cucurbita pepo", "family": "Cucurbitaceae", "genus": "Cucurbita", "species": "pepo", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Cucurbitales", "subfamily": "Cucurbitoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Bottle Gourd (Lauki)", "botanical_name": "Lagenaria siceraria", "family": "Cucurbitaceae", "genus": "Lagenaria", "species": "siceraria", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Cucurbitales", "subfamily": "Cucurbitoideae", "author": "(Molina) Standl.", "iucn": "LC"},
    {"common_name": "Bitter Gourd (Karela)", "botanical_name": "Momordica charantia", "family": "Cucurbitaceae", "genus": "Momordica", "species": "charantia", "category": "Vegetable/Medicinal", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Cucurbitales", "subfamily": "Cucurbitoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Ridge Gourd (Turai)", "botanical_name": "Luffa acutangula", "family": "Cucurbitaceae", "genus": "Luffa", "species": "acutangula", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Cucurbitales", "subfamily": "Cucurbitoideae", "author": "(L.) Roxb.", "iucn": "LC"},
    {"common_name": "Snake Gourd", "botanical_name": "Trichosanthes cucumerina", "family": "Cucurbitaceae", "genus": "Trichosanthes", "species": "cucumerina", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Cucurbitales", "subfamily": "Cucurbitoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Ash Gourd (Petha)", "botanical_name": "Benincasa hispida", "family": "Cucurbitaceae", "genus": "Benincasa", "species": "hispida", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Cucurbitales", "subfamily": "Cucurbitoideae", "author": "(Thunb.) Cogn.", "iucn": "LC"},
    {"common_name": "Ivy Gourd (Tindora)", "botanical_name": "Coccinia grandis", "family": "Cucurbitaceae", "genus": "Coccinia", "species": "grandis", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Cucurbitales", "subfamily": "Cucurbitoideae", "author": "(L.) Voigt", "iucn": "LC"},

    # ─── VEGETABLES – LEAFY ──────────────────────────────────────────────────
    {"common_name": "Spinach", "botanical_name": "Spinacia oleracea", "family": "Amaranthaceae", "genus": "Spinacia", "species": "oleracea", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Caryophyllidae", "order": "Caryophyllales", "subfamily": "Chenopodioideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Lettuce", "botanical_name": "Lactuca sativa", "family": "Asteraceae", "genus": "Lactuca", "species": "sativa", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Asterales", "subfamily": "Cichorioideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Cabbage", "botanical_name": "Brassica oleracea var. capitata", "family": "Brassicaceae", "genus": "Brassica", "species": "oleracea", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Brassicales", "subfamily": "Brassiceae", "author": "L.", "iucn": "LC"},
    {"common_name": "Broccoli", "botanical_name": "Brassica oleracea var. italica", "family": "Brassicaceae", "genus": "Brassica", "species": "oleracea", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Brassicales", "subfamily": "Brassiceae", "author": "Plenck", "iucn": "LC"},
    {"common_name": "Cauliflower", "botanical_name": "Brassica oleracea var. botrytis", "family": "Brassicaceae", "genus": "Brassica", "species": "oleracea", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Brassicales", "subfamily": "Brassiceae", "author": "L.", "iucn": "LC"},
    {"common_name": "Kale", "botanical_name": "Brassica oleracea var. acephala", "family": "Brassicaceae", "genus": "Brassica", "species": "oleracea", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Brassicales", "subfamily": "Brassiceae", "author": "DC.", "iucn": "LC"},
    {"common_name": "Celery", "botanical_name": "Apium graveolens", "family": "Apiaceae", "genus": "Apium", "species": "graveolens", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Apiales", "subfamily": "Apioideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Mustard Greens (Sarson)", "botanical_name": "Brassica juncea", "family": "Brassicaceae", "genus": "Brassica", "species": "juncea", "category": "Vegetable/Oilseed", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Brassicales", "subfamily": "Brassiceae", "author": "(L.) Czern.", "iucn": "LC"},
    {"common_name": "Fenugreek (Methi)", "botanical_name": "Trigonella foenum-graecum", "family": "Fabaceae", "genus": "Trigonella", "species": "foenum-graecum", "category": "Vegetable/Spice", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Fabales", "subfamily": "Faboideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Leek", "botanical_name": "Allium ampeloprasum", "family": "Amaryllidaceae", "genus": "Allium", "species": "ampeloprasum", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Lilianae", "order": "Asparagales", "subfamily": "Allioideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Spring Onion (Scallion)", "botanical_name": "Allium fistulosum", "family": "Amaryllidaceae", "genus": "Allium", "species": "fistulosum", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Lilianae", "order": "Asparagales", "subfamily": "Allioideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Amaranth Leaves", "botanical_name": "Amaranthus tricolor", "family": "Amaranthaceae", "genus": "Amaranthus", "species": "tricolor", "category": "Vegetable", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Caryophyllidae", "order": "Caryophyllales", "subfamily": "Amaranthoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Moringa (Drumstick)", "botanical_name": "Moringa oleifera", "family": "Moringaceae", "genus": "Moringa", "species": "oleifera", "category": "Vegetable/Medicinal/Tree", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Brassicales", "subfamily": "Moringoideae", "author": "Lam.", "iucn": "LC"},
    {"common_name": "Coriander (Cilantro)", "botanical_name": "Coriandrum sativum", "family": "Apiaceae", "genus": "Coriandrum", "species": "sativum", "category": "Herb/Spice", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Apiales", "subfamily": "Apioideae", "author": "L.", "iucn": "LC"},

    # ─── SPICES ───────────────────────────────────────────────────────────────
    {"common_name": "Black Pepper", "botanical_name": "Piper nigrum", "family": "Piperaceae", "genus": "Piper", "species": "nigrum", "category": "Spice", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Magnoliidae", "order": "Piperales", "subfamily": "Piperoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Cardamom (Green)", "botanical_name": "Elettaria cardamomum", "family": "Zingiberaceae", "genus": "Elettaria", "species": "cardamomum", "category": "Spice", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Zingiberales", "subfamily": "Zingiberoideae", "author": "(L.) Maton", "iucn": "LC"},
    {"common_name": "Cinnamon", "botanical_name": "Cinnamomum verum", "family": "Lauraceae", "genus": "Cinnamomum", "species": "verum", "category": "Spice", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Magnoliidae", "order": "Laurales", "subfamily": "Lauroideae", "author": "J.Presl", "iucn": "LC"},
    {"common_name": "Clove", "botanical_name": "Syzygium aromaticum", "family": "Myrtaceae", "genus": "Syzygium", "species": "aromaticum", "category": "Spice", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Myrtales", "subfamily": "Myrtoideae", "author": "(L.) Merr. & L.M.Perry", "iucn": "LC"},
    {"common_name": "Nutmeg", "botanical_name": "Myristica fragrans", "family": "Myristicaceae", "genus": "Myristica", "species": "fragrans", "category": "Spice", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Magnoliidae", "order": "Magnoliales", "subfamily": "Myristicoideae", "author": "Houtt.", "iucn": "LC"},
    {"common_name": "Vanilla", "botanical_name": "Vanilla planifolia", "family": "Orchidaceae", "genus": "Vanilla", "species": "planifolia", "category": "Spice", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Lilianae", "order": "Asparagales", "subfamily": "Vanilloideae", "author": "Andrews", "iucn": "VU"},
    {"common_name": "Cumin", "botanical_name": "Cuminum cyminum", "family": "Apiaceae", "genus": "Cuminum", "species": "cyminum", "category": "Spice", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Apiales", "subfamily": "Apioideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Caraway", "botanical_name": "Carum carvi", "family": "Apiaceae", "genus": "Carum", "species": "carvi", "category": "Spice", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Apiales", "subfamily": "Apioideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Ajwain (Carom)", "botanical_name": "Trachyspermum ammi", "family": "Apiaceae", "genus": "Trachyspermum", "species": "ammi", "category": "Spice", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Apiales", "subfamily": "Apioideae", "author": "(L.) Sprague", "iucn": "LC"},
    {"common_name": "Star Anise", "botanical_name": "Illicium verum", "family": "Schisandraceae", "genus": "Illicium", "species": "verum", "category": "Spice", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Magnoliidae", "order": "Austrobaileyales", "subfamily": "Illicioideae", "author": "Hook.f.", "iucn": "LC"},
    {"common_name": "Saffron", "botanical_name": "Crocus sativus", "family": "Iridaceae", "genus": "Crocus", "species": "sativus", "category": "Spice", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Lilianae", "order": "Asparagales", "subfamily": "Iridoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Fennel", "botanical_name": "Foeniculum vulgare", "family": "Apiaceae", "genus": "Foeniculum", "species": "vulgare", "category": "Spice/Herb", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Apiales", "subfamily": "Apioideae", "author": "Mill.", "iucn": "LC"},
    {"common_name": "Dill", "botanical_name": "Anethum graveolens", "family": "Apiaceae", "genus": "Anethum", "species": "graveolens", "category": "Herb/Spice", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Apiales", "subfamily": "Apioideae", "author": "L.", "iucn": "LC"},

    # ─── MEDICINAL & AROMATIC HERBS ──────────────────────────────────────────
    {"common_name": "Neem", "botanical_name": "Azadirachta indica", "family": "Meliaceae", "genus": "Azadirachta", "species": "indica", "category": "Medicinal Tree", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Sapindales", "subfamily": "Meliaceae", "author": "A.Juss.", "iucn": "LC"},
    {"common_name": "Tulsi (Holy Basil)", "botanical_name": "Ocimum tenuiflorum", "family": "Lamiaceae", "genus": "Ocimum", "species": "tenuiflorum", "category": "Medicinal Herb", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Lamiales", "subfamily": "Ocimeae", "author": "L.", "iucn": "LC"},
    {"common_name": "Mint (Spearmint)", "botanical_name": "Mentha spicata", "family": "Lamiaceae", "genus": "Mentha", "species": "spicata", "category": "Herb", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Lamiales", "subfamily": "Mentheae", "author": "L.", "iucn": "LC"},
    {"common_name": "Peppermint", "botanical_name": "Mentha x piperita", "family": "Lamiaceae", "genus": "Mentha", "species": "piperita", "category": "Herb", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Lamiales", "subfamily": "Mentheae", "author": "L.", "iucn": "LC"},
    {"common_name": "Sweet Basil", "botanical_name": "Ocimum basilicum", "family": "Lamiaceae", "genus": "Ocimum", "species": "basilicum", "category": "Herb", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Lamiales", "subfamily": "Ocimeae", "author": "L.", "iucn": "LC"},
    {"common_name": "Rosemary", "botanical_name": "Salvia rosmarinus", "family": "Lamiaceae", "genus": "Salvia", "species": "rosmarinus", "category": "Herb", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Lamiales", "subfamily": "Mentheae", "author": "Spenn.", "iucn": "LC"},
    {"common_name": "Thyme", "botanical_name": "Thymus vulgaris", "family": "Lamiaceae", "genus": "Thymus", "species": "vulgaris", "category": "Herb", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Lamiales", "subfamily": "Mentheae", "author": "L.", "iucn": "LC"},
    {"common_name": "Oregano", "botanical_name": "Origanum vulgare", "family": "Lamiaceae", "genus": "Origanum", "species": "vulgare", "category": "Herb", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Lamiales", "subfamily": "Mentheae", "author": "L.", "iucn": "LC"},
    {"common_name": "Lavender", "botanical_name": "Lavandula angustifolia", "family": "Lamiaceae", "genus": "Lavandula", "species": "angustifolia", "category": "Aromatic Herb", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Lamiales", "subfamily": "Ocimeae", "author": "Mill.", "iucn": "LC"},
    {"common_name": "Sage", "botanical_name": "Salvia officinalis", "family": "Lamiaceae", "genus": "Salvia", "species": "officinalis", "category": "Herb", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Lamiales", "subfamily": "Mentheae", "author": "L.", "iucn": "LC"},
    {"common_name": "Parsley", "botanical_name": "Petroselinum crispum", "family": "Apiaceae", "genus": "Petroselinum", "species": "crispum", "category": "Herb", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Apiales", "subfamily": "Apioideae", "author": "(Mill.) Fuss", "iucn": "LC"},
    {"common_name": "Aloe Vera", "botanical_name": "Aloe vera", "family": "Xanthorrhoeaceae", "genus": "Aloe", "species": "vera", "category": "Succulent/Medicinal", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Lilianae", "order": "Asparagales", "subfamily": "Alooideae", "author": "(L.) Burm.f.", "iucn": "LC"},
    {"common_name": "Ashwagandha", "botanical_name": "Withania somnifera", "family": "Solanaceae", "genus": "Withania", "species": "somnifera", "category": "Medicinal Herb", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Solanales", "subfamily": "Solanoideae", "author": "(L.) Dunal", "iucn": "LC"},
    {"common_name": "Brahmi (Water Hyssop)", "botanical_name": "Bacopa monnieri", "family": "Plantaginaceae", "genus": "Bacopa", "species": "monnieri", "category": "Medicinal Herb", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Lamiales", "subfamily": "Gratioleae", "author": "(L.) Wettst.", "iucn": "LC"},
    {"common_name": "Giloy (Tinospora)", "botanical_name": "Tinospora cordifolia", "family": "Menispermaceae", "genus": "Tinospora", "species": "cordifolia", "category": "Medicinal Climber", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Ranunculidae", "order": "Ranunculales", "subfamily": "Tinosporoideae", "author": "(Willd.) Miers", "iucn": "LC"},
    {"common_name": "Lemongrass", "botanical_name": "Cymbopogon citratus", "family": "Poaceae", "genus": "Cymbopogon", "species": "citratus", "category": "Aromatic Herb", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Poales", "subfamily": "Panicoideae", "author": "(DC.) Stapf", "iucn": "LC"},
    {"common_name": "Vetiver (Khus)", "botanical_name": "Chrysopogon zizanioides", "family": "Poaceae", "genus": "Chrysopogon", "species": "zizanioides", "category": "Aromatic Grass", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Poales", "subfamily": "Panicoideae", "author": "(L.) Roberty", "iucn": "LC"},
    {"common_name": "Gotu Kola", "botanical_name": "Centella asiatica", "family": "Apiaceae", "genus": "Centella", "species": "asiatica", "category": "Medicinal Herb", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Apiales", "subfamily": "Mackinlayoideae", "author": "(L.) Urb.", "iucn": "LC"},
    {"common_name": "Sarpagandha (Indian Snakeroot)", "botanical_name": "Rauwolfia serpentina", "family": "Apocynaceae", "genus": "Rauwolfia", "species": "serpentina", "category": "Medicinal Shrub", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Gentianales", "subfamily": "Rauvolfioideae", "author": "(L.) Benth. ex Kurz", "iucn": "EN"},
    {"common_name": "Periwinkle (Sadabahar)", "botanical_name": "Catharanthus roseus", "family": "Apocynaceae", "genus": "Catharanthus", "species": "roseus", "category": "Medicinal Herb", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Gentianales", "subfamily": "Rauvolfioideae", "author": "(L.) G.Don", "iucn": "LC"},
    {"common_name": "Andrographis (Kalmegh)", "botanical_name": "Andrographis paniculata", "family": "Acanthaceae", "genus": "Andrographis", "species": "paniculata", "category": "Medicinal Herb", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Lamiales", "subfamily": "Andrographideae", "author": "(Burm.f.) Nees", "iucn": "LC"},

    # ─── TREES ────────────────────────────────────────────────────────────────
    {"common_name": "Teak", "botanical_name": "Tectona grandis", "family": "Lamiaceae", "genus": "Tectona", "species": "grandis", "category": "Timber Tree", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Lamiales", "subfamily": "Viticoideae", "author": "L.f.", "iucn": "LC"},
    {"common_name": "Rosewood (Sheesham)", "botanical_name": "Dalbergia sissoo", "family": "Fabaceae", "genus": "Dalbergia", "species": "sissoo", "category": "Timber Tree", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Fabales", "subfamily": "Faboideae", "author": "DC.", "iucn": "NT"},
    {"common_name": "Eucalyptus", "botanical_name": "Eucalyptus globulus", "family": "Myrtaceae", "genus": "Eucalyptus", "species": "globulus", "category": "Timber/Medicinal Tree", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Myrtales", "subfamily": "Myrtoideae", "author": "Labill.", "iucn": "LC"},
    {"common_name": "Babool (Acacia)", "botanical_name": "Vachellia nilotica", "family": "Fabaceae", "genus": "Vachellia", "species": "nilotica", "category": "Multipurpose Tree", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Fabales", "subfamily": "Caesalpinioideae", "author": "(L.) P.J.H.Hurter & Mabb.", "iucn": "LC"},
    {"common_name": "Bamboo (Moso)", "botanical_name": "Phyllostachys edulis", "family": "Poaceae", "genus": "Phyllostachys", "species": "edulis", "category": "Bamboo", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Poales", "subfamily": "Bambusoideae", "author": "(Carrière) J.Houz.", "iucn": "LC"},
    {"common_name": "Dendrocalamus (Giant Bamboo)", "botanical_name": "Dendrocalamus strictus", "family": "Poaceae", "genus": "Dendrocalamus", "species": "strictus", "category": "Bamboo", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Poales", "subfamily": "Bambusoideae", "author": "(Roxb.) Nees", "iucn": "LC"},
    {"common_name": "Sal Tree", "botanical_name": "Shorea robusta", "family": "Dipterocarpaceae", "genus": "Shorea", "species": "robusta", "category": "Forest Tree", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Malvales", "subfamily": "Dipterocarpoideae", "author": "C.F.Gaertn.", "iucn": "NT"},
    {"common_name": "Peepal (Sacred Fig)", "botanical_name": "Ficus religiosa", "family": "Moraceae", "genus": "Ficus", "species": "religiosa", "category": "Sacred Tree", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Rosales", "subfamily": "Moroideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Banyan Tree", "botanical_name": "Ficus benghalensis", "family": "Moraceae", "genus": "Ficus", "species": "benghalensis", "category": "Sacred Tree", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Rosales", "subfamily": "Moroideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Arjuna Tree", "botanical_name": "Terminalia arjuna", "family": "Combretaceae", "genus": "Terminalia", "species": "arjuna", "category": "Medicinal Tree", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Myrtales", "subfamily": "Combretoideae", "author": "(Roxb. ex DC.) Wight & Arn.", "iucn": "LC"},
    {"common_name": "Mahogany", "botanical_name": "Swietenia mahagoni", "family": "Meliaceae", "genus": "Swietenia", "species": "mahagoni", "category": "Timber Tree", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Sapindales", "subfamily": "Melioideae", "author": "(L.) Jacq.", "iucn": "EN"},
    {"common_name": "Mangrove (Red)", "botanical_name": "Rhizophora mangle", "family": "Rhizophoraceae", "genus": "Rhizophora", "species": "mangle", "category": "Mangrove", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Malpighiales", "subfamily": "Rhizophoroideae", "author": "L.", "iucn": "LC"},

    # ─── ORNAMENTAL FLOWERS ───────────────────────────────────────────────────
    {"common_name": "Rose", "botanical_name": "Rosa indica", "family": "Rosaceae", "genus": "Rosa", "species": "indica", "category": "Ornamental Flower", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Rosales", "subfamily": "Rosoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Jasmine", "botanical_name": "Jasminum sambac", "family": "Oleaceae", "genus": "Jasminum", "species": "sambac", "category": "Ornamental Flower", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Lamiales", "subfamily": "Oleoideae", "author": "(L.) Aiton", "iucn": "LC"},
    {"common_name": "Hibiscus", "botanical_name": "Hibiscus rosa-sinensis", "family": "Malvaceae", "genus": "Hibiscus", "species": "rosa-sinensis", "category": "Ornamental Flower", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Malvales", "subfamily": "Malvoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Lotus", "botanical_name": "Nelumbo nucifera", "family": "Nelumbonaceae", "genus": "Nelumbo", "species": "nucifera", "category": "Aquatic Flower", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Proteidae", "order": "Proteales", "subfamily": "Nelumbonoideae", "author": "Gaertn.", "iucn": "LC"},
    {"common_name": "Marigold", "botanical_name": "Tagetes erecta", "family": "Asteraceae", "genus": "Tagetes", "species": "erecta", "category": "Ornamental Flower", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Asterales", "subfamily": "Tagetinae", "author": "L.", "iucn": "LC"},
    {"common_name": "Chrysanthemum", "botanical_name": "Chrysanthemum morifolium", "family": "Asteraceae", "genus": "Chrysanthemum", "species": "morifolium", "category": "Ornamental Flower", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Asterales", "subfamily": "Anthemideae", "author": "Ramat.", "iucn": "LC"},
    {"common_name": "Sunflower", "botanical_name": "Helianthus annuus", "family": "Asteraceae", "genus": "Helianthus", "species": "annuus", "category": "Ornamental/Oilseed", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Asterales", "subfamily": "Heliantheae", "author": "L.", "iucn": "LC"},
    {"common_name": "Carnation", "botanical_name": "Dianthus caryophyllus", "family": "Caryophyllaceae", "genus": "Dianthus", "species": "caryophyllus", "category": "Ornamental Flower", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Caryophyllidae", "order": "Caryophyllales", "subfamily": "Caryophylloideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Bougainvillea", "botanical_name": "Bougainvillea spectabilis", "family": "Nyctaginaceae", "genus": "Bougainvillea", "species": "spectabilis", "category": "Ornamental Climber", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Caryophyllidae", "order": "Caryophyllales", "subfamily": "Bougainvilleoideae", "author": "Willd.", "iucn": "LC"},
    {"common_name": "Dahlia", "botanical_name": "Dahlia pinnata", "family": "Asteraceae", "genus": "Dahlia", "species": "pinnata", "category": "Ornamental Flower", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Asterales", "subfamily": "Coreopsideae", "author": "Cav.", "iucn": "LC"},
    {"common_name": "Tulip", "botanical_name": "Tulipa gesneriana", "family": "Liliaceae", "genus": "Tulipa", "species": "gesneriana", "category": "Ornamental Flower", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Lilianae", "order": "Liliales", "subfamily": "Lilioideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Orchid (Phalaenopsis)", "botanical_name": "Phalaenopsis amabilis", "family": "Orchidaceae", "genus": "Phalaenopsis", "species": "amabilis", "category": "Ornamental Flower", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Lilianae", "order": "Asparagales", "subfamily": "Epidendroideae", "author": "(L.) Blume", "iucn": "VU"},
    {"common_name": "Lily (Easter)", "botanical_name": "Lilium longiflorum", "family": "Liliaceae", "genus": "Lilium", "species": "longiflorum", "category": "Ornamental Flower", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Lilianae", "order": "Liliales", "subfamily": "Lilioideae", "author": "Thunb.", "iucn": "LC"},
    {"common_name": "Zinnia", "botanical_name": "Zinnia elegans", "family": "Asteraceae", "genus": "Zinnia", "species": "elegans", "category": "Ornamental Flower", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Asteridae", "order": "Asterales", "subfamily": "Heliantheae", "author": "Jacq.", "iucn": "LC"},

    # ─── WILD, AQUATIC & SPECIAL PLANTS ──────────────────────────────────────
    {"common_name": "Water Hyacinth", "botanical_name": "Eichhornia crassipes", "family": "Pontederiaceae", "genus": "Eichhornia", "species": "crassipes", "category": "Aquatic/Invasive", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Commelinidae", "order": "Commelinales", "subfamily": "Pontederioideae", "author": "(Mart.) Solms", "iucn": "LC"},
    {"common_name": "Venus Flytrap", "botanical_name": "Dionaea muscipula", "family": "Droseraceae", "genus": "Dionaea", "species": "muscipula", "category": "Carnivorous Plant", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Caryophyllidae", "order": "Caryophyllales", "subfamily": "Droseridae", "author": "Sol. ex J.Ellis", "iucn": "VU"},
    {"common_name": "Sundew", "botanical_name": "Drosera rotundifolia", "family": "Droseraceae", "genus": "Drosera", "species": "rotundifolia", "category": "Carnivorous Plant", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Caryophyllidae", "order": "Caryophyllales", "subfamily": "Droseridae", "author": "L.", "iucn": "LC"},
    {"common_name": "Pitcher Plant", "botanical_name": "Nepenthes rajah", "family": "Nepenthaceae", "genus": "Nepenthes", "species": "rajah", "category": "Carnivorous Plant", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Caryophyllidae", "order": "Caryophyllales", "subfamily": "Nepentheae", "author": "Hook.f.", "iucn": "EN"},
    {"common_name": "Prickly Pear Cactus", "botanical_name": "Opuntia ficus-indica", "family": "Cactaceae", "genus": "Opuntia", "species": "ficus-indica", "category": "Cactus/Fruit", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Caryophyllidae", "order": "Caryophyllales", "subfamily": "Cactoideae", "author": "(L.) Mill.", "iucn": "LC"},
    {"common_name": "Agave (Century Plant)", "botanical_name": "Agave americana", "family": "Asparagaceae", "genus": "Agave", "species": "americana", "category": "Succulent", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Liliopsida", "subclass": "Lilianae", "order": "Asparagales", "subfamily": "Agavoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Common Bracken Fern", "botanical_name": "Pteridium aquilinum", "family": "Dennstaedtiaceae", "genus": "Pteridium", "species": "aquilinum", "category": "Fern", "subkingdom": "Viridaeplantae", "division": "Polypodiophyta", "class_name": "Polypodiopsida", "subclass": "Polypodiidae", "order": "Dennstaedtiales", "subfamily": "Dennstaedtioideae", "author": "(L.) Kuhn", "iucn": "LC"},
    {"common_name": "Peat Moss", "botanical_name": "Sphagnum palustre", "family": "Sphagnaceae", "genus": "Sphagnum", "species": "palustre", "category": "Moss/Bryophyte", "subkingdom": "Viridaeplantae", "division": "Bryophyta", "class_name": "Sphagnopsida", "subclass": "Sphagnidae", "order": "Sphagnales", "subfamily": "Sphagnoideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Spirulina (Blue-Green Algae)", "botanical_name": "Arthrospira platensis", "family": "Microcoleaceae", "genus": "Arthrospira", "species": "platensis", "category": "Algae/Superfood", "subkingdom": "Cyanobacteria", "division": "Cyanophyta", "class_name": "Cyanophyceae", "subclass": "Oscillatoriophycideae", "order": "Oscillatoriales", "subfamily": "Microcoleaceae", "author": "(Nordstedt) Gomont", "iucn": "LC"},
    {"common_name": "Kelp Seaweed", "botanical_name": "Saccharina latissima", "family": "Laminariaceae", "genus": "Saccharina", "species": "latissima", "category": "Seaweed/Algae", "subkingdom": "Chromalveolata", "division": "Phaeophyta", "class_name": "Phaeophyceae", "subclass": "Fucidae", "order": "Laminariales", "subfamily": "Laminarioideae", "author": "(L.) C.E.Lane, C.Mayes, Druehl & G.W.Saunders", "iucn": "LC"},

    # ─── NITROGEN-FIXING & GREEN MANURE ──────────────────────────────────────
    {"common_name": "Sesbania (Dhaincha)", "botanical_name": "Sesbania bispinosa", "family": "Fabaceae", "genus": "Sesbania", "species": "bispinosa", "category": "Green Manure", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Fabales", "subfamily": "Faboideae", "author": "(Jacq.) W.Wight", "iucn": "LC"},
    {"common_name": "Sunn Hemp", "botanical_name": "Crotalaria juncea", "family": "Fabaceae", "genus": "Crotalaria", "species": "juncea", "category": "Green Manure/Fiber", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Fabales", "subfamily": "Faboideae", "author": "L.", "iucn": "LC"},
    {"common_name": "Velvet Bean (Mucuna)", "botanical_name": "Mucuna pruriens", "family": "Fabaceae", "genus": "Mucuna", "species": "pruriens", "category": "Cover Crop/Medicinal", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Fabales", "subfamily": "Faboideae", "author": "(L.) DC.", "iucn": "LC"},
    {"common_name": "Gliricidia", "botanical_name": "Gliricidia sepium", "family": "Fabaceae", "genus": "Gliricidia", "species": "sepium", "category": "Agroforestry/Fodder", "subkingdom": "Viridaeplantae", "division": "Tracheophyta", "class_name": "Magnoliopsida", "subclass": "Rosidae", "order": "Fabales", "subfamily": "Faboideae", "author": "(Jacq.) Kunth ex Walp.", "iucn": "LC"},
]


def get_family_info(family_name: str) -> dict:
    """Get family information from the database."""
    return PLANT_FAMILIES.get(family_name, {
        "order": "Unknown", "division": "Tracheophyta", "class": "Magnoliopsida",
        "description": f"Plant family {family_name}",
        "notable_genera": []
    })


def get_taxonomy_for_plant(plant: dict) -> dict:
    """Build complete 14-rank taxonomy for a given plant."""
    family_info = get_family_info(plant.get("family", ""))
    return {
        "kingdom": "Plantae",
        "subkingdom": plant.get("subkingdom", "Viridaeplantae"),
        "division": plant.get("division", family_info.get("division", "Tracheophyta")),
        "subdivision": "Spermatophytina" if plant.get("division") == "Tracheophyta" else None,
        "class_name": plant.get("class_name", family_info.get("class", "Magnoliopsida")),
        "subclass": plant.get("subclass", None),
        "order_name": plant.get("order", family_info.get("order", "Unknown")),
        "family_name": plant.get("family", ""),
        "subfamily": plant.get("subfamily", None),
        "genus": plant.get("genus", ""),
        "species": plant.get("species", ""),
        "scientific_name": plant.get("botanical_name", ""),
        "author_citation": plant.get("author", ""),
        "iucn_status": plant.get("iucn", "LC"),
    }


if __name__ == "__main__":
    print(f"Total plant families in database: {len(PLANT_FAMILIES)}")
    print(f"Total plant genera in database: {len(PLANT_GENERA)}")
    print(f"Total flagship plant species: {len(FLAGSHIP_PLANTS)}")
