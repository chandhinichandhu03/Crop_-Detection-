-- Agro Doctor Botanical Intelligence Dataset PostgreSQL Dump
-- Generated at: 2026-06-26 21:20:52

BEGIN;

DROP TABLE IF EXISTS taxonomy_full CASCADE;
CREATE TABLE taxonomy_full (
    id INTEGER PRIMARY KEY NOT NULL,
    kingdom VARCHAR(100) NULL,
    subkingdom VARCHAR(100) NULL,
    division VARCHAR(100) NULL,
    subdivision VARCHAR(100) NULL,
    class_name VARCHAR(100) NULL,
    subclass VARCHAR(100) NULL,
    order_name VARCHAR(100) NULL,
    family_name VARCHAR(100) NULL,
    subfamily VARCHAR(100) NULL,
    tribe VARCHAR(100) NULL,
    genus VARCHAR(200) NULL,
    species VARCHAR(200) NULL,
    common_name VARCHAR(200) NULL,
    botanical_name VARCHAR(300) NULL,
    author_citation VARCHAR(200) NULL,
    iucn_status VARCHAR(10) NULL,
    category VARCHAR(100) NULL,
    family_description VARCHAR(255) NULL,
    genera_species_count INTEGER NULL,
    created_at TIMESTAMP NULL
);

-- Data for taxonomy_full (223 rows)
INSERT INTO taxonomy_full (id, kingdom, subkingdom, division, subdivision, class_name, subclass, order_name, family_name, subfamily, tribe, genus, species, common_name, botanical_name, author_citation, iucn_status, category, family_description, genera_species_count, created_at) VALUES
    (1, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Poales', 'Poaceae', 'Oryzoideae', NULL, 'Oryza', 'sativa', 'Rice', 'Oryza sativa', 'L.', 'LC', 'Cereal', 'Grass family; cereals and grains - most economically important plant family', 24, '2026-06-26 15:47:47'),
    (2, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Poales', 'Poaceae', 'Pooideae', NULL, 'Triticum', 'aestivum', 'Wheat', 'Triticum aestivum', 'L.', 'LC', 'Cereal', 'Grass family; cereals and grains - most economically important plant family', 30, '2026-06-26 15:47:47'),
    (3, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Poales', 'Poaceae', 'Panicoideae', NULL, 'Zea', 'mays', 'Maize (Corn)', 'Zea mays', 'L.', 'LC', 'Cereal', 'Grass family; cereals and grains - most economically important plant family', 4, '2026-06-26 15:47:47'),
    (4, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Poales', 'Poaceae', 'Pooideae', NULL, 'Hordeum', 'vulgare', 'Barley', 'Hordeum vulgare', 'L.', 'LC', 'Cereal', 'Grass family; cereals and grains - most economically important plant family', 32, '2026-06-26 15:47:47'),
    (5, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Poales', 'Poaceae', 'Pooideae', NULL, 'Avena', 'sativa', 'Oat', 'Avena sativa', 'L.', 'LC', 'Cereal', 'Grass family; cereals and grains - most economically important plant family', 29, '2026-06-26 15:47:47'),
    (6, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Poales', 'Poaceae', 'Panicoideae', NULL, 'Sorghum', 'bicolor', 'Sorghum', 'Sorghum bicolor', '(L.) Moench', 'LC', 'Cereal', 'Grass family; cereals and grains - most economically important plant family', 31, '2026-06-26 15:47:47'),
    (7, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Poales', 'Poaceae', 'Panicoideae', NULL, 'Pennisetum', 'glaucum', 'Pearl Millet', 'Pennisetum glaucum', '(L.) R.Br.', 'LC', 'Millet', 'Grass family; cereals and grains - most economically important plant family', 140, '2026-06-26 15:47:47'),
    (8, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Poales', 'Poaceae', 'Chloridoideae', NULL, 'Eleusine', 'coracana', 'Finger Millet', 'Eleusine coracana', '(L.) Gaertn.', 'LC', 'Millet', 'Grass family; cereals and grains - most economically important plant family', 9, '2026-06-26 15:47:47'),
    (9, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Poales', 'Poaceae', 'Panicoideae', NULL, 'Setaria', 'italica', 'Foxtail Millet', 'Setaria italica', '(L.) P.Beauv.', 'LC', 'Millet', 'Grass family; cereals and grains - most economically important plant family', 140, '2026-06-26 15:47:47'),
    (10, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Poales', 'Poaceae', 'Panicoideae', NULL, 'Panicum', 'miliaceum', 'Proso Millet', 'Panicum miliaceum', 'L.', 'LC', 'Millet', 'Grass family; cereals and grains - most economically important plant family', 450, '2026-06-26 15:47:47'),
    (11, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Poales', 'Poaceae', 'Panicoideae', NULL, 'Echinochloa', 'frumentacea', 'Barnyard Millet', 'Echinochloa frumentacea', 'Link', 'LC', 'Millet', 'Grass family; cereals and grains - most economically important plant family', 50, '2026-06-26 15:47:47'),
    (12, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Poales', 'Poaceae', 'Panicoideae', NULL, 'Paspalum', 'scrobiculatum', 'Kodo Millet', 'Paspalum scrobiculatum', 'L.', 'LC', 'Millet', 'Grass family; cereals and grains - most economically important plant family', 400, '2026-06-26 15:47:47'),
    (13, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Poales', 'Poaceae', 'Panicoideae', NULL, 'Panicum', 'sumatrense', 'Little Millet', 'Panicum sumatrense', 'Roth ex Roem. & Schult.', 'LC', 'Millet', 'Grass family; cereals and grains - most economically important plant family', 450, '2026-06-26 15:47:47'),
    (14, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Caryophyllidae', 'Caryophyllales', 'Polygonaceae', 'Polygonoideae', NULL, 'Fagopyrum', 'esculentum', 'Buckwheat', 'Fagopyrum esculentum', 'Moench', 'LC', 'Pseudocereal', 'Buckwheat/Dock family', 25, '2026-06-26 15:47:47'),
    (15, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Caryophyllidae', 'Caryophyllales', 'Amaranthaceae', 'Chenopodioideae', NULL, 'Chenopodium', 'quinoa', 'Quinoa', 'Chenopodium quinoa', 'Willd.', 'LC', 'Pseudocereal', 'Amaranth family; includes beet, spinach, quinoa', 200, '2026-06-26 15:47:47'),
    (16, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Caryophyllidae', 'Caryophyllales', 'Amaranthaceae', 'Amaranthoideae', NULL, 'Amaranthus', 'hypochondriacus', 'Amaranth Grain', 'Amaranthus hypochondriacus', 'L.', 'LC', 'Pseudocereal', 'Amaranth family; includes beet, spinach, quinoa', 75, '2026-06-26 15:47:47'),
    (17, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Poales', 'Poaceae', 'Pooideae', NULL, 'Triticum', 'durum', 'Durum Wheat', 'Triticum durum', 'Desf.', 'LC', 'Cereal', 'Grass family; cereals and grains - most economically important plant family', 30, '2026-06-26 15:47:47'),
    (18, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Poales', 'Poaceae', 'Pooideae', NULL, 'Secale', 'cereale', 'Rye', 'Secale cereale', 'L.', 'LC', 'Cereal', 'Grass family; cereals and grains - most economically important plant family', 0, '2026-06-26 15:47:47'),
    (19, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Poales', 'Poaceae', 'Pooideae', NULL, 'Triticosecale', 'rimpaui', 'Triticale', 'Triticosecale rimpaui', 'Wittm.', 'LC', 'Cereal', 'Grass family; cereals and grains - most economically important plant family', 0, '2026-06-26 15:47:47'),
    (20, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Fabales', 'Fabaceae', 'Faboideae', NULL, 'Glycine', 'max', 'Soybean', 'Glycine max', '(L.) Merr.', 'LC', 'Pulse', 'Legume/Pea family; world''s second largest food plant family', 18, '2026-06-26 15:47:47'),
    (21, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Fabales', 'Fabaceae', 'Faboideae', NULL, 'Cicer', 'arietinum', 'Chickpea (Bengal Gram)', 'Cicer arietinum', 'L.', 'LC', 'Pulse', 'Legume/Pea family; world''s second largest food plant family', 43, '2026-06-26 15:47:47'),
    (22, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Fabales', 'Fabaceae', 'Faboideae', NULL, 'Lens', 'culinaris', 'Lentil', 'Lens culinaris', 'Medik.', 'LC', 'Pulse', 'Legume/Pea family; world''s second largest food plant family', 6, '2026-06-26 15:47:47'),
    (23, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Fabales', 'Fabaceae', 'Faboideae', NULL, 'Cajanus', 'cajan', 'Pigeon Pea (Red Gram)', 'Cajanus cajan', '(L.) Millsp.', 'LC', 'Pulse', 'Legume/Pea family; world''s second largest food plant family', 32, '2026-06-26 15:47:47'),
    (24, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Fabales', 'Fabaceae', 'Faboideae', NULL, 'Vigna', 'radiata', 'Mung Bean (Green Gram)', 'Vigna radiata', '(L.) R.Wilczek', 'LC', 'Pulse', 'Legume/Pea family; world''s second largest food plant family', 100, '2026-06-26 15:47:47'),
    (25, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Fabales', 'Fabaceae', 'Faboideae', NULL, 'Vigna', 'mungo', 'Black Gram (Urad)', 'Vigna mungo', '(L.) Hepper', 'LC', 'Pulse', 'Legume/Pea family; world''s second largest food plant family', 100, '2026-06-26 15:47:47'),
    (26, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Fabales', 'Fabaceae', 'Faboideae', NULL, 'Vigna', 'unguiculata', 'Cowpea', 'Vigna unguiculata', '(L.) Walp.', 'LC', 'Pulse', 'Legume/Pea family; world''s second largest food plant family', 100, '2026-06-26 15:47:47'),
    (27, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Fabales', 'Fabaceae', 'Faboideae', NULL, 'Phaseolus', 'vulgaris', 'Kidney Bean', 'Phaseolus vulgaris', 'L.', 'LC', 'Pulse', 'Legume/Pea family; world''s second largest food plant family', 80, '2026-06-26 15:47:47'),
    (28, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Fabales', 'Fabaceae', 'Faboideae', NULL, 'Phaseolus', 'lunatus', 'Lima Bean', 'Phaseolus lunatus', 'L.', 'LC', 'Pulse', 'Legume/Pea family; world''s second largest food plant family', 80, '2026-06-26 15:47:47'),
    (29, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Fabales', 'Fabaceae', 'Faboideae', NULL, 'Pisum', 'sativum', 'Field Pea', 'Pisum sativum', 'L.', 'LC', 'Pulse', 'Legume/Pea family; world''s second largest food plant family', 2, '2026-06-26 15:47:47'),
    (30, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Fabales', 'Fabaceae', 'Faboideae', NULL, 'Vicia', 'faba', 'Faba Bean (Broad Bean)', 'Vicia faba', 'L.', 'LC', 'Pulse', 'Legume/Pea family; world''s second largest food plant family', 140, '2026-06-26 15:47:47'),
    (31, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Fabales', 'Fabaceae', 'Faboideae', NULL, 'Arachis', 'hypogaea', 'Groundnut (Peanut)', 'Arachis hypogaea', 'L.', 'LC', 'Oilseed/Pulse', 'Legume/Pea family; world''s second largest food plant family', 80, '2026-06-26 15:47:47'),
    (32, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Fabales', 'Fabaceae', 'Faboideae', NULL, 'Vigna', 'aconitifolia', 'Moth Bean', 'Vigna aconitifolia', '(Jacq.) Marechal', 'LC', 'Pulse', 'Legume/Pea family; world''s second largest food plant family', 100, '2026-06-26 15:47:47'),
    (33, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Fabales', 'Fabaceae', 'Faboideae', NULL, 'Macrotyloma', 'uniflorum', 'Horse Gram', 'Macrotyloma uniflorum', '(Lam.) Verdc.', 'LC', 'Pulse', 'Legume/Pea family; world''s second largest food plant family', 0, '2026-06-26 15:47:47'),
    (34, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Fabales', 'Fabaceae', 'Faboideae', NULL, 'Cyamopsis', 'tetragonoloba', 'Cluster Bean (Guar)', 'Cyamopsis tetragonoloba', '(L.) Taub.', 'LC', 'Pulse', 'Legume/Pea family; world''s second largest food plant family', 0, '2026-06-26 15:47:47'),
    (35, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Asterales', 'Asteraceae', 'Asteroideae', NULL, 'Helianthus', 'annuus', 'Sunflower', 'Helianthus annuus', 'L.', 'LC', 'Oilseed', 'Daisy/Composite family; world''s largest flowering plant family', 70, '2026-06-26 15:47:47'),
    (36, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Brassicales', 'Brassicaceae', 'Brassiceae', NULL, 'Brassica', 'napus', 'Rapeseed / Canola', 'Brassica napus', 'L.', 'LC', 'Oilseed', 'Mustard/Cabbage family; cruciferous vegetables', 40, '2026-06-26 15:47:47'),
    (37, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Malvales', 'Malvaceae', 'Malvoideae', NULL, 'Gossypium', 'hirsutum', 'Cotton', 'Gossypium hirsutum', 'L.', 'LC', 'Fiber/Oilseed', 'Mallow family; cotton, hibiscus, cacao, durian', 50, '2026-06-26 15:47:47'),
    (38, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Lamiales', 'Pedaliaceae', 'Sesameae', NULL, 'Sesamum', 'indicum', 'Sesame', 'Sesamum indicum', 'L.', 'LC', 'Oilseed', '', 36, '2026-06-26 15:47:47'),
    (39, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Malpighiales', 'Euphorbiaceae', 'Acalyphoideae', NULL, 'Ricinus', 'communis', 'Castor', 'Ricinus communis', 'L.', 'LC', 'Oilseed', 'Spurge family; includes cassava, rubber, castor', 1, '2026-06-26 15:47:47'),
    (40, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Malpighiales', 'Linaceae', 'Linoideae', NULL, 'Linum', 'usitatissimum', 'Linseed / Flax', 'Linum usitatissimum', 'L.', 'LC', 'Fiber/Oilseed', '', 200, '2026-06-26 15:47:47'),
    (41, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Arecales', 'Arecaceae', 'Arecoideae', NULL, 'Elaeis', 'guineensis', 'Oil Palm', 'Elaeis guineensis', 'Jacq.', 'LC', 'Oilseed/Plantation', 'Palm family; coconut, date, oil palm', 2, '2026-06-26 15:47:47'),
    (42, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Malpighiales', 'Euphorbiaceae', 'Crotonoideae', NULL, 'Jatropha', 'curcas', 'Jatropha (Biofuel)', 'Jatropha curcas', 'L.', 'LC', 'Biofuel/Oilseed', 'Spurge family; includes cassava, rubber, castor', 175, '2026-06-26 15:47:47'),
    (43, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Brassicales', 'Brassicaceae', 'Brassiceae', NULL, 'Brassica', 'nigra', 'Mustard (Black)', 'Brassica nigra', '(L.) K.Koch', 'LC', 'Oilseed/Spice', 'Mustard/Cabbage family; cruciferous vegetables', 40, '2026-06-26 15:47:47'),
    (44, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Asterales', 'Asteraceae', 'Carduoideae', NULL, 'Carthamus', 'tinctorius', 'Safflower', 'Carthamus tinctorius', 'L.', 'LC', 'Oilseed', 'Daisy/Composite family; world''s largest flowering plant family', 0, '2026-06-26 15:47:47'),
    (45, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Poales', 'Poaceae', 'Panicoideae', NULL, 'Saccharum', 'officinarum', 'Sugarcane', 'Saccharum officinarum', 'L.', 'LC', 'Sugar Crop', 'Grass family; cereals and grains - most economically important plant family', 37, '2026-06-26 15:47:47'),
    (46, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Caryophyllidae', 'Caryophyllales', 'Amaranthaceae', 'Chenopodioideae', NULL, 'Beta', 'vulgaris', 'Sugar Beet', 'Beta vulgaris subsp. vulgaris', 'L.', 'LC', 'Sugar Crop', 'Amaranth family; includes beet, spinach, quinoa', 6, '2026-06-26 15:47:47'),
    (47, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Asterales', 'Asteraceae', 'Eupatorieae', NULL, 'Stevia', 'rebaudiana', 'Stevia', 'Stevia rebaudiana', 'Bertoni', 'LC', 'Sugar Crop', 'Daisy/Composite family; world''s largest flowering plant family', 0, '2026-06-26 15:47:47'),
    (48, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Malvales', 'Malvaceae', 'Grewioideae', NULL, 'Corchorus', 'olitorius', 'Jute', 'Corchorus olitorius', 'L.', 'LC', 'Fiber Crop', 'Mallow family; cotton, hibiscus, cacao, durian', 0, '2026-06-26 15:47:47'),
    (49, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Rosales', 'Cannabaceae', 'Cannaboideae', NULL, 'Cannabis', 'sativa', 'Hemp', 'Cannabis sativa', 'L.', 'LC', 'Fiber/Industrial', 'Hemp family; includes hemp and hops', 0, '2026-06-26 15:47:47'),
    (50, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Lilianae', 'Asparagales', 'Asparagaceae', 'Agavoideae', NULL, 'Agave', 'sisalana', 'Sisal', 'Agave sisalana', 'Perrine', 'LC', 'Fiber Crop', 'Asparagus family; includes agave, yucca', 208, '2026-06-26 15:47:47'),
    (51, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Gentianales', 'Rubiaceae', 'Ixoroideae', NULL, 'Coffea', 'arabica', 'Coffee (Arabica)', 'Coffea arabica', 'L.', 'EN', 'Beverage/Plantation', 'Coffee/Bedstraw family', 125, '2026-06-26 15:47:47'),
    (52, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Gentianales', 'Rubiaceae', 'Ixoroideae', NULL, 'Coffea', 'canephora', 'Coffee (Robusta)', 'Coffea canephora', 'Pierre ex A.Froehner', 'LC', 'Beverage/Plantation', 'Coffee/Bedstraw family', 125, '2026-06-26 15:47:47'),
    (53, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Ericales', 'Theaceae', 'Theoideae', NULL, 'Camellia', 'sinensis', 'Tea', 'Camellia sinensis', '(L.) Kuntze', 'LC', 'Beverage/Plantation', 'Tea family', 119, '2026-06-26 15:47:47'),
    (54, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Malvales', 'Malvaceae', 'Byttnerioideae', NULL, 'Theobroma', 'cacao', 'Cacao (Cocoa)', 'Theobroma cacao', 'L.', 'LC', 'Beverage/Plantation', 'Mallow family; cotton, hibiscus, cacao, durian', 22, '2026-06-26 15:47:47'),
    (55, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Malpighiales', 'Euphorbiaceae', 'Crotonoideae', NULL, 'Hevea', 'brasiliensis', 'Rubber Tree', 'Hevea brasiliensis', '(Willd. ex A.Juss.) Müll.Arg.', 'LC', 'Plantation/Industrial', 'Spurge family; includes cassava, rubber, castor', 11, '2026-06-26 15:47:47'),
    (56, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Sapindales', 'Anacardiaceae', 'Anacardioideae', NULL, 'Mangifera', 'indica', 'Mango', 'Mangifera indica', 'L.', 'LC', 'Fruit', 'Cashew/Mango family', 69, '2026-06-26 15:47:47'),
    (57, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Zingiberales', 'Musaceae', 'Musoideae', NULL, 'Musa', 'acuminata', 'Banana', 'Musa acuminata', 'Colla', 'LC', 'Fruit', 'Banana family', 70, '2026-06-26 15:47:47'),
    (58, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Poales', 'Bromeliaceae', 'Bromelioideae', NULL, 'Ananas', 'comosus', 'Pineapple', 'Ananas comosus', '(L.) Merr.', 'LC', 'Fruit', 'Pineapple family', 8, '2026-06-26 15:47:47'),
    (59, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Brassicales', 'Caricaceae', 'Caricaceae', NULL, 'Carica', 'papaya', 'Papaya', 'Carica papaya', 'L.', 'LC', 'Fruit', 'Papaya family', 22, '2026-06-26 15:47:47'),
    (60, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Rosales', 'Moraceae', 'Moroideae', NULL, 'Artocarpus', 'heterophyllus', 'Jackfruit', 'Artocarpus heterophyllus', 'Lam.', 'LC', 'Fruit', 'Mulberry family; includes fig, breadfruit, jackfruit', 70, '2026-06-26 15:47:47'),
    (61, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Myrtales', 'Myrtaceae', 'Myrtoideae', NULL, 'Psidium', 'guajava', 'Guava', 'Psidium guajava', 'L.', 'LC', 'Fruit', 'Myrtle family; includes guava, eucalyptus, clove', 100, '2026-06-26 15:47:47'),
    (62, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Arecales', 'Arecaceae', 'Arecoideae', NULL, 'Cocos', 'nucifera', 'Coconut', 'Cocos nucifera', 'L.', 'LC', 'Fruit/Plantation', 'Palm family; coconut, date, oil palm', 1, '2026-06-26 15:47:47'),
    (63, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Arecales', 'Arecaceae', 'Arecoideae', NULL, 'Phoenix', 'dactylifera', 'Date Palm', 'Phoenix dactylifera', 'L.', 'LC', 'Fruit', 'Palm family; coconut, date, oil palm', 14, '2026-06-26 15:47:47'),
    (64, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Myrtales', 'Lythraceae', 'Punicoideae', NULL, 'Punica', 'granatum', 'Pomegranate', 'Punica granatum', 'L.', 'LC', 'Fruit', 'Loosestrife family; includes pomegranate and henna', 2, '2026-06-26 15:47:47'),
    (65, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Caryophyllidae', 'Caryophyllales', 'Cactaceae', 'Cactoideae', NULL, 'Selenicereus', 'undatus', 'Dragon Fruit (Pitaya)', 'Selenicereus undatus', '(Haw.) D.R.Hunt', 'LC', 'Fruit', 'Cactus family; succulent xerophytes', 20, '2026-06-26 15:47:47'),
    (66, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Magnoliidae', 'Laurales', 'Lauraceae', 'Perseoideae', NULL, 'Persea', 'americana', 'Avocado', 'Persea americana', 'Mill.', 'LC', 'Fruit', 'Laurel family; avocado, cinnamon, bay laurel', 200, '2026-06-26 15:47:47'),
    (67, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Ericales', 'Actinidiaceae', 'Actinidioideae', NULL, 'Actinidia', 'deliciosa', 'Kiwifruit', 'Actinidia deliciosa', '(A.Chev.) C.F.Liang & A.R.Ferguson', 'LC', 'Fruit', 'Kiwifruit family', 54, '2026-06-26 15:47:47'),
    (68, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Sapindales', 'Sapindaceae', 'Sapindoideae', NULL, 'Litchi', 'chinensis', 'Lychee', 'Litchi chinensis', 'Sonn.', 'LC', 'Fruit', 'Soapberry family; includes lychee, longan, rambutan, maple', 1, '2026-06-26 15:47:47'),
    (69, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Sapindales', 'Sapindaceae', 'Sapindoideae', NULL, 'Dimocarpus', 'longan', 'Longan', 'Dimocarpus longan', 'Lour.', 'LC', 'Fruit', 'Soapberry family; includes lychee, longan, rambutan, maple', 3, '2026-06-26 15:47:47'),
    (70, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Sapindales', 'Sapindaceae', 'Sapindoideae', NULL, 'Nephelium', 'lappaceum', 'Rambutan', 'Nephelium lappaceum', 'L.', 'LC', 'Fruit', 'Soapberry family; includes lychee, longan, rambutan, maple', 22, '2026-06-26 15:47:47'),
    (71, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Malvales', 'Malvaceae', 'Helicteroideae', NULL, 'Durio', 'zibethinus', 'Durian', 'Durio zibethinus', 'D.Murray', 'LC', 'Fruit', 'Mallow family; cotton, hibiscus, cacao, durian', 30, '2026-06-26 15:47:47'),
    (72, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Malpighiales', 'Passifloraceae', 'Passifloroideae', NULL, 'Passiflora', 'edulis', 'Passion Fruit', 'Passiflora edulis', 'Sims', 'LC', 'Fruit', 'Passion flower family', 550, '2026-06-26 15:47:47'),
    (73, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Ericales', 'Sapotaceae', 'Mimusopoideae', NULL, 'Manilkara', 'zapota', 'Sapodilla (Sapota)', 'Manilkara zapota', '(L.) P.Royen', 'LC', 'Fruit', 'Sapodilla family; chicle, shea butter', 85, '2026-06-26 15:47:47'),
    (74, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Rosales', 'Moraceae', 'Moroideae', NULL, 'Ficus', 'carica', 'Fig', 'Ficus carica', 'L.', 'LC', 'Fruit', 'Mulberry family; includes fig, breadfruit, jackfruit', 850, '2026-06-26 15:47:47'),
    (75, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Rosales', 'Moraceae', 'Moroideae', NULL, 'Morus', 'alba', 'Mulberry', 'Morus alba', 'L.', 'LC', 'Fruit', 'Mulberry family; includes fig, breadfruit, jackfruit', 16, '2026-06-26 15:47:47'),
    (76, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Magnoliidae', 'Magnoliales', 'Annonaceae', 'Annonoideae', NULL, 'Annona', 'squamosa', 'Custard Apple', 'Annona squamosa', 'L.', 'LC', 'Fruit', 'Custard apple / Soursop family', 166, '2026-06-26 15:47:47'),
    (77, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Magnoliidae', 'Magnoliales', 'Annonaceae', 'Annonoideae', NULL, 'Annona', 'muricata', 'Soursop (Graviola)', 'Annona muricata', 'L.', 'LC', 'Fruit', 'Custard apple / Soursop family', 166, '2026-06-26 15:47:47'),
    (78, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Oxalidales', 'Oxalidaceae', 'Oxalidoideae', NULL, 'Averrhoa', 'carambola', 'Star Fruit (Carambola)', 'Averrhoa carambola', 'L.', 'LC', 'Fruit', 'Wood sorrel family; includes star fruit', 2, '2026-06-26 15:47:47'),
    (79, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Malpighiales', 'Clusiaceae', 'Clusioideae', NULL, 'Garcinia', 'mangostana', 'Mangosteen', 'Garcinia mangostana', 'L.', 'LC', 'Fruit', 'Mangosteen family (Guttiferae)', 400, '2026-06-26 15:47:47'),
    (80, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Rosales', 'Moraceae', 'Moroideae', NULL, 'Artocarpus', 'altilis', 'Breadfruit', 'Artocarpus altilis', '(Parkinson) Fosberg', 'LC', 'Fruit', 'Mulberry family; includes fig, breadfruit, jackfruit', 70, '2026-06-26 15:47:47'),
    (81, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Fabales', 'Fabaceae', 'Caesalpinioideae', NULL, 'Tamarindus', 'indica', 'Tamarind', 'Tamarindus indica', 'L.', 'LC', 'Fruit/Spice', 'Legume/Pea family; world''s second largest food plant family', 0, '2026-06-26 15:47:47'),
    (82, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Myrtales', 'Myrtaceae', 'Myrtoideae', NULL, 'Syzygium', 'cumini', 'Java Plum (Jamun)', 'Syzygium cumini', '(L.) Skeels', 'LC', 'Fruit', 'Myrtle family; includes guava, eucalyptus, clove', 1200, '2026-06-26 15:47:47'),
    (83, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Malpighiales', 'Phyllanthaceae', 'Phyllanthoideae', NULL, 'Phyllanthus', 'emblica', 'Amla (Indian Gooseberry)', 'Phyllanthus emblica', 'L.', 'LC', 'Fruit/Medicinal', '', 800, '2026-06-26 15:47:47'),
    (84, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Sapindales', 'Rutaceae', 'Aurantioideae', NULL, 'Aegle', 'marmelos', 'Wood Apple (Bael)', 'Aegle marmelos', '(L.) Corrêa', 'LC', 'Fruit/Medicinal', 'Citrus family; all citrus fruits', 0, '2026-06-26 15:47:47'),
    (85, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Zingiberales', 'Musaceae', 'Musoideae', NULL, 'Musa', 'paradisiaca', 'Banana (Plantain)', 'Musa paradisiaca', 'L.', 'LC', 'Fruit', 'Banana family', 70, '2026-06-26 15:47:47'),
    (86, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Sapindales', 'Rutaceae', 'Aurantioideae', NULL, 'Citrus', 'sinensis', 'Sweet Orange', 'Citrus sinensis', '(L.) Osbeck', 'LC', 'Fruit', 'Citrus family; all citrus fruits', 25, '2026-06-26 15:47:47'),
    (87, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Sapindales', 'Rutaceae', 'Aurantioideae', NULL, 'Citrus', 'limon', 'Lemon', 'Citrus limon', '(L.) Osbeck', 'LC', 'Fruit', 'Citrus family; all citrus fruits', 25, '2026-06-26 15:47:47'),
    (88, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Sapindales', 'Rutaceae', 'Aurantioideae', NULL, 'Citrus', 'aurantiifolia', 'Lime', 'Citrus aurantiifolia', '(Christm.) Swingle', 'LC', 'Fruit', 'Citrus family; all citrus fruits', 25, '2026-06-26 15:47:47'),
    (89, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Sapindales', 'Rutaceae', 'Aurantioideae', NULL, 'Citrus', 'reticulata', 'Mandarin / Tangerine', 'Citrus reticulata', 'Blanco', 'LC', 'Fruit', 'Citrus family; all citrus fruits', 25, '2026-06-26 15:47:47'),
    (90, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Sapindales', 'Rutaceae', 'Aurantioideae', NULL, 'Citrus', 'paradisi', 'Grapefruit', 'Citrus paradisi', 'Macfad.', 'LC', 'Fruit', 'Citrus family; all citrus fruits', 25, '2026-06-26 15:47:47'),
    (91, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Sapindales', 'Rutaceae', 'Aurantioideae', NULL, 'Citrus', 'maxima', 'Pomelo', 'Citrus maxima', '(Burm.) Merr.', 'LC', 'Fruit', 'Citrus family; all citrus fruits', 25, '2026-06-26 15:47:47'),
    (92, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Sapindales', 'Rutaceae', 'Aurantioideae', NULL, 'Fortunella', 'japonica', 'Kumquat', 'Fortunella japonica', '(Thunb.) Swingle', 'LC', 'Fruit', 'Citrus family; all citrus fruits', 0, '2026-06-26 15:47:47'),
    (93, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Rosales', 'Rosaceae', 'Maloideae', NULL, 'Malus', 'domestica', 'Apple', 'Malus domestica', 'Borkh.', 'LC', 'Fruit', 'Rose family; includes apples, pears, cherries, plums, strawberries', 55, '2026-06-26 15:47:47'),
    (94, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Rosales', 'Rosaceae', 'Maloideae', NULL, 'Pyrus', 'communis', 'Pear', 'Pyrus communis', 'L.', 'LC', 'Fruit', 'Rose family; includes apples, pears, cherries, plums, strawberries', 87, '2026-06-26 15:47:47'),
    (95, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Rosales', 'Rosaceae', 'Amygdaloideae', NULL, 'Prunus', 'persica', 'Peach', 'Prunus persica', '(L.) Batsch', 'LC', 'Fruit', 'Rose family; includes apples, pears, cherries, plums, strawberries', 430, '2026-06-26 15:47:47'),
    (96, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Rosales', 'Rosaceae', 'Amygdaloideae', NULL, 'Prunus', 'domestica', 'Plum', 'Prunus domestica', 'L.', 'LC', 'Fruit', 'Rose family; includes apples, pears, cherries, plums, strawberries', 430, '2026-06-26 15:47:47'),
    (97, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Rosales', 'Rosaceae', 'Amygdaloideae', NULL, 'Prunus', 'avium', 'Cherry (Sweet)', 'Prunus avium', '(L.) L.', 'LC', 'Fruit', 'Rose family; includes apples, pears, cherries, plums, strawberries', 430, '2026-06-26 15:47:47'),
    (98, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Rosales', 'Rosaceae', 'Amygdaloideae', NULL, 'Prunus', 'armeniaca', 'Apricot', 'Prunus armeniaca', 'L.', 'NT', 'Fruit', 'Rose family; includes apples, pears, cherries, plums, strawberries', 430, '2026-06-26 15:47:47'),
    (99, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Rosales', 'Rosaceae', 'Rosoideae', NULL, 'Fragaria', 'ananassa', 'Strawberry', 'Fragaria x ananassa', 'Duchesne ex Rozier', 'LC', 'Fruit', 'Rose family; includes apples, pears, cherries, plums, strawberries', 20, '2026-06-26 15:47:47'),
    (100, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Vitales', 'Vitaceae', 'Vitoideae', NULL, 'Vitis', 'vinifera', 'Grape', 'Vitis vinifera', 'L.', 'LC', 'Fruit', 'Grape family', 79, '2026-06-26 15:47:47');
INSERT INTO taxonomy_full (id, kingdom, subkingdom, division, subdivision, class_name, subclass, order_name, family_name, subfamily, tribe, genus, species, common_name, botanical_name, author_citation, iucn_status, category, family_description, genera_species_count, created_at) VALUES
    (101, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Ericales', 'Ericaceae', 'Vaccinioideae', NULL, 'Vaccinium', 'corymbosum', 'Blueberry', 'Vaccinium corymbosum', 'L.', 'LC', 'Fruit', 'Heath family; blueberries, cranberries, rhododendron', 450, '2026-06-26 15:47:47'),
    (102, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Rosales', 'Rosaceae', 'Rosoideae', NULL, 'Rubus', 'idaeus', 'Raspberry', 'Rubus idaeus', 'L.', 'LC', 'Fruit', 'Rose family; includes apples, pears, cherries, plums, strawberries', 750, '2026-06-26 15:47:47'),
    (103, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Rosales', 'Rosaceae', 'Rosoideae', NULL, 'Rubus', 'fruticosus', 'Blackberry', 'Rubus fruticosus', 'L. agg.', 'LC', 'Fruit', 'Rose family; includes apples, pears, cherries, plums, strawberries', 750, '2026-06-26 15:47:47'),
    (104, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Ericales', 'Ericaceae', 'Vaccinioideae', NULL, 'Vaccinium', 'macrocarpon', 'Cranberry', 'Vaccinium macrocarpon', 'Aiton', 'LC', 'Fruit', 'Heath family; blueberries, cranberries, rhododendron', 450, '2026-06-26 15:47:47'),
    (105, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Saxifragales', 'Grossulariaceae', 'Grossularioideae', NULL, 'Ribes', 'uva-crispa', 'Gooseberry', 'Ribes uva-crispa', 'L.', 'LC', 'Fruit', '', 150, '2026-06-26 15:47:47'),
    (106, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Ericales', 'Ebenaceae', 'Ebenoideae', NULL, 'Diospyros', 'kaki', 'Persimmon', 'Diospyros kaki', 'Thunb.', 'LC', 'Fruit', 'Ebony/Persimmon family', 700, '2026-06-26 15:47:47'),
    (107, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Rosales', 'Rosaceae', 'Amygdaloideae', NULL, 'Prunus', 'dulcis', 'Almond', 'Prunus dulcis', '(Mill.) D.A.Webb', 'LC', 'Nut/Fruit', 'Rose family; includes apples, pears, cherries, plums, strawberries', 430, '2026-06-26 15:47:47'),
    (108, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Fagales', 'Juglandaceae', 'Juglandoideae', NULL, 'Juglans', 'regia', 'Walnut', 'Juglans regia', 'L.', 'NT', 'Nut/Fruit', 'Walnut family', 0, '2026-06-26 15:47:47'),
    (109, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Cucurbitales', 'Cucurbitaceae', 'Cucurbitoideae', NULL, 'Citrullus', 'lanatus', 'Watermelon', 'Citrullus lanatus', '(Thunb.) Matsum. & Nakai', 'LC', 'Fruit/Vegetable', 'Gourd/Squash family; cucumbers, melons, pumpkins', 4, '2026-06-26 15:47:47'),
    (110, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Cucurbitales', 'Cucurbitaceae', 'Cucurbitoideae', NULL, 'Cucumis', 'melo', 'Muskmelon / Cantaloupe', 'Cucumis melo', 'L.', 'LC', 'Fruit/Vegetable', 'Gourd/Squash family; cucumbers, melons, pumpkins', 52, '2026-06-26 15:47:47'),
    (111, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Solanales', 'Solanaceae', 'Solanoideae', NULL, 'Solanum', 'lycopersicum', 'Tomato', 'Solanum lycopersicum', 'L.', 'LC', 'Vegetable', 'Nightshade family; tomato, potato, pepper, tobacco', 1500, '2026-06-26 15:47:47'),
    (112, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Solanales', 'Solanaceae', 'Solanoideae', NULL, 'Solanum', 'tuberosum', 'Potato', 'Solanum tuberosum', 'L.', 'LC', 'Vegetable', 'Nightshade family; tomato, potato, pepper, tobacco', 1500, '2026-06-26 15:47:47'),
    (113, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Lilianae', 'Asparagales', 'Amaryllidaceae', 'Allioideae', NULL, 'Allium', 'cepa', 'Onion', 'Allium cepa', 'L.', 'LC', 'Vegetable', '', 920, '2026-06-26 15:47:47'),
    (114, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Lilianae', 'Asparagales', 'Amaryllidaceae', 'Allioideae', NULL, 'Allium', 'sativum', 'Garlic', 'Allium sativum', 'L.', 'LC', 'Vegetable/Spice', '', 920, '2026-06-26 15:47:47'),
    (115, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Zingiberales', 'Zingiberaceae', 'Zingiberoideae', NULL, 'Zingiber', 'officinale', 'Ginger', 'Zingiber officinale', 'Roscoe', 'LC', 'Spice/Medicinal', 'Ginger family; ginger, turmeric, cardamom', 140, '2026-06-26 15:47:47'),
    (116, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Zingiberales', 'Zingiberaceae', 'Zingiberoideae', NULL, 'Curcuma', 'longa', 'Turmeric', 'Curcuma longa', 'L.', 'LC', 'Spice/Medicinal', 'Ginger family; ginger, turmeric, cardamom', 100, '2026-06-26 15:47:47'),
    (117, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Apiales', 'Apiaceae', 'Apioideae', NULL, 'Daucus', 'carota', 'Carrot', 'Daucus carota', 'L.', 'LC', 'Vegetable', 'Carrot/Parsley family; umbellifers', 25, '2026-06-26 15:47:47'),
    (118, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Brassicales', 'Brassicaceae', 'Brassiceae', NULL, 'Raphanus', 'sativus', 'Radish', 'Raphanus sativus', 'L.', 'LC', 'Vegetable', 'Mustard/Cabbage family; cruciferous vegetables', 3, '2026-06-26 15:47:47'),
    (119, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Brassicales', 'Brassicaceae', 'Brassiceae', NULL, 'Brassica', 'rapa', 'Turnip', 'Brassica rapa', 'L.', 'LC', 'Vegetable', 'Mustard/Cabbage family; cruciferous vegetables', 40, '2026-06-26 15:47:47'),
    (120, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Solanales', 'Convolvulaceae', 'Convolvuloideae', NULL, 'Ipomoea', 'batatas', 'Sweet Potato', 'Ipomoea batatas', '(L.) Lam.', 'LC', 'Vegetable', 'Morning glory family; sweet potato', 650, '2026-06-26 15:47:47'),
    (121, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Lilianae', 'Dioscoreales', 'Dioscoreaceae', 'Dioscoreoideae', NULL, 'Dioscorea', 'alata', 'Yam', 'Dioscorea alata', 'L.', 'LC', 'Vegetable', 'Yam family', 870, '2026-06-26 15:47:47'),
    (122, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Malpighiales', 'Euphorbiaceae', 'Crotonoideae', NULL, 'Manihot', 'esculenta', 'Cassava (Tapioca)', 'Manihot esculenta', 'Crantz', 'LC', 'Vegetable/Tuber', 'Spurge family; includes cassava, rubber, castor', 100, '2026-06-26 15:47:47'),
    (123, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Alismatanae', 'Alismatales', 'Araceae', 'Aroideae', NULL, 'Colocasia', 'esculenta', 'Taro (Arvi)', 'Colocasia esculenta', '(L.) Schott', 'LC', 'Vegetable/Tuber', 'Arum family; includes taro, colocasia', 25, '2026-06-26 15:47:47'),
    (124, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Alismatanae', 'Alismatales', 'Araceae', 'Aroideae', NULL, 'Amorphophallus', 'paeoniifolius', 'Elephant Foot Yam', 'Amorphophallus paeoniifolius', '(Dennst.) Nicolson', 'LC', 'Vegetable/Tuber', 'Arum family; includes taro, colocasia', 0, '2026-06-26 15:47:47'),
    (125, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Solanales', 'Solanaceae', 'Solanoideae', NULL, 'Solanum', 'melongena', 'Brinjal (Eggplant)', 'Solanum melongena', 'L.', 'LC', 'Vegetable', 'Nightshade family; tomato, potato, pepper, tobacco', 1500, '2026-06-26 15:47:47'),
    (126, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Solanales', 'Solanaceae', 'Solanoideae', NULL, 'Capsicum', 'annuum', 'Chilli (Hot Pepper)', 'Capsicum annuum', 'L.', 'LC', 'Vegetable/Spice', 'Nightshade family; tomato, potato, pepper, tobacco', 40, '2026-06-26 15:47:47'),
    (127, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Solanales', 'Solanaceae', 'Solanoideae', NULL, 'Capsicum', 'annuum', 'Bell Pepper (Capsicum)', 'Capsicum annuum var. grossum', '(Willd.) Sendtn.', 'LC', 'Vegetable', 'Nightshade family; tomato, potato, pepper, tobacco', 40, '2026-06-26 15:47:47'),
    (128, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Malvales', 'Malvaceae', 'Malvoideae', NULL, 'Abelmoschus', 'esculentus', 'Okra (Ladies Finger)', 'Abelmoschus esculentus', '(L.) Moench', 'LC', 'Vegetable', 'Mallow family; cotton, hibiscus, cacao, durian', 15, '2026-06-26 15:47:47'),
    (129, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Cucurbitales', 'Cucurbitaceae', 'Cucurbitoideae', NULL, 'Cucumis', 'sativus', 'Cucumber', 'Cucumis sativus', 'L.', 'LC', 'Vegetable', 'Gourd/Squash family; cucumbers, melons, pumpkins', 52, '2026-06-26 15:47:47'),
    (130, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Cucurbitales', 'Cucurbitaceae', 'Cucurbitoideae', NULL, 'Cucurbita', 'pepo', 'Pumpkin', 'Cucurbita pepo', 'L.', 'LC', 'Vegetable', 'Gourd/Squash family; cucumbers, melons, pumpkins', 15, '2026-06-26 15:47:47'),
    (131, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Cucurbitales', 'Cucurbitaceae', 'Cucurbitoideae', NULL, 'Lagenaria', 'siceraria', 'Bottle Gourd (Lauki)', 'Lagenaria siceraria', '(Molina) Standl.', 'LC', 'Vegetable', 'Gourd/Squash family; cucumbers, melons, pumpkins', 6, '2026-06-26 15:47:47'),
    (132, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Cucurbitales', 'Cucurbitaceae', 'Cucurbitoideae', NULL, 'Momordica', 'charantia', 'Bitter Gourd (Karela)', 'Momordica charantia', 'L.', 'LC', 'Vegetable/Medicinal', 'Gourd/Squash family; cucumbers, melons, pumpkins', 60, '2026-06-26 15:47:47'),
    (133, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Cucurbitales', 'Cucurbitaceae', 'Cucurbitoideae', NULL, 'Luffa', 'acutangula', 'Ridge Gourd (Turai)', 'Luffa acutangula', '(L.) Roxb.', 'LC', 'Vegetable', 'Gourd/Squash family; cucumbers, melons, pumpkins', 8, '2026-06-26 15:47:47'),
    (134, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Cucurbitales', 'Cucurbitaceae', 'Cucurbitoideae', NULL, 'Trichosanthes', 'cucumerina', 'Snake Gourd', 'Trichosanthes cucumerina', 'L.', 'LC', 'Vegetable', 'Gourd/Squash family; cucumbers, melons, pumpkins', 100, '2026-06-26 15:47:47'),
    (135, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Cucurbitales', 'Cucurbitaceae', 'Cucurbitoideae', NULL, 'Benincasa', 'hispida', 'Ash Gourd (Petha)', 'Benincasa hispida', '(Thunb.) Cogn.', 'LC', 'Vegetable', 'Gourd/Squash family; cucumbers, melons, pumpkins', 1, '2026-06-26 15:47:47'),
    (136, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Cucurbitales', 'Cucurbitaceae', 'Cucurbitoideae', NULL, 'Coccinia', 'grandis', 'Ivy Gourd (Tindora)', 'Coccinia grandis', '(L.) Voigt', 'LC', 'Vegetable', 'Gourd/Squash family; cucumbers, melons, pumpkins', 30, '2026-06-26 15:47:47'),
    (137, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Caryophyllidae', 'Caryophyllales', 'Amaranthaceae', 'Chenopodioideae', NULL, 'Spinacia', 'oleracea', 'Spinach', 'Spinacia oleracea', 'L.', 'LC', 'Vegetable', 'Amaranth family; includes beet, spinach, quinoa', 3, '2026-06-26 15:47:47'),
    (138, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Asterales', 'Asteraceae', 'Cichorioideae', NULL, 'Lactuca', 'sativa', 'Lettuce', 'Lactuca sativa', 'L.', 'LC', 'Vegetable', 'Daisy/Composite family; world''s largest flowering plant family', 75, '2026-06-26 15:47:47'),
    (139, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Brassicales', 'Brassicaceae', 'Brassiceae', NULL, 'Brassica', 'oleracea', 'Cabbage', 'Brassica oleracea var. capitata', 'L.', 'LC', 'Vegetable', 'Mustard/Cabbage family; cruciferous vegetables', 40, '2026-06-26 15:47:47'),
    (140, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Brassicales', 'Brassicaceae', 'Brassiceae', NULL, 'Brassica', 'oleracea', 'Broccoli', 'Brassica oleracea var. italica', 'Plenck', 'LC', 'Vegetable', 'Mustard/Cabbage family; cruciferous vegetables', 40, '2026-06-26 15:47:47'),
    (141, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Brassicales', 'Brassicaceae', 'Brassiceae', NULL, 'Brassica', 'oleracea', 'Cauliflower', 'Brassica oleracea var. botrytis', 'L.', 'LC', 'Vegetable', 'Mustard/Cabbage family; cruciferous vegetables', 40, '2026-06-26 15:47:47'),
    (142, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Brassicales', 'Brassicaceae', 'Brassiceae', NULL, 'Brassica', 'oleracea', 'Kale', 'Brassica oleracea var. acephala', 'DC.', 'LC', 'Vegetable', 'Mustard/Cabbage family; cruciferous vegetables', 40, '2026-06-26 15:47:47'),
    (143, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Apiales', 'Apiaceae', 'Apioideae', NULL, 'Apium', 'graveolens', 'Celery', 'Apium graveolens', 'L.', 'LC', 'Vegetable', 'Carrot/Parsley family; umbellifers', 0, '2026-06-26 15:47:47'),
    (144, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Brassicales', 'Brassicaceae', 'Brassiceae', NULL, 'Brassica', 'juncea', 'Mustard Greens (Sarson)', 'Brassica juncea', '(L.) Czern.', 'LC', 'Vegetable/Oilseed', 'Mustard/Cabbage family; cruciferous vegetables', 40, '2026-06-26 15:47:47'),
    (145, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Fabales', 'Fabaceae', 'Faboideae', NULL, 'Trigonella', 'foenum-graecum', 'Fenugreek (Methi)', 'Trigonella foenum-graecum', 'L.', 'LC', 'Vegetable/Spice', 'Legume/Pea family; world''s second largest food plant family', 135, '2026-06-26 15:47:47'),
    (146, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Lilianae', 'Asparagales', 'Amaryllidaceae', 'Allioideae', NULL, 'Allium', 'ampeloprasum', 'Leek', 'Allium ampeloprasum', 'L.', 'LC', 'Vegetable', '', 920, '2026-06-26 15:47:47'),
    (147, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Lilianae', 'Asparagales', 'Amaryllidaceae', 'Allioideae', NULL, 'Allium', 'fistulosum', 'Spring Onion (Scallion)', 'Allium fistulosum', 'L.', 'LC', 'Vegetable', '', 920, '2026-06-26 15:47:47'),
    (148, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Caryophyllidae', 'Caryophyllales', 'Amaranthaceae', 'Amaranthoideae', NULL, 'Amaranthus', 'tricolor', 'Amaranth Leaves', 'Amaranthus tricolor', 'L.', 'LC', 'Vegetable', 'Amaranth family; includes beet, spinach, quinoa', 75, '2026-06-26 15:47:47'),
    (149, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Brassicales', 'Moringaceae', 'Moringoideae', NULL, 'Moringa', 'oleifera', 'Moringa (Drumstick)', 'Moringa oleifera', 'Lam.', 'LC', 'Vegetable/Medicinal/Tree', 'Moringa/Drumstick tree family', 13, '2026-06-26 15:47:47'),
    (150, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Apiales', 'Apiaceae', 'Apioideae', NULL, 'Coriandrum', 'sativum', 'Coriander (Cilantro)', 'Coriandrum sativum', 'L.', 'LC', 'Herb/Spice', 'Carrot/Parsley family; umbellifers', 2, '2026-06-26 15:47:47'),
    (151, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Magnoliidae', 'Piperales', 'Piperaceae', 'Piperoideae', NULL, 'Piper', 'nigrum', 'Black Pepper', 'Piper nigrum', 'L.', 'LC', 'Spice', 'Pepper family', 3000, '2026-06-26 15:47:47'),
    (152, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Zingiberales', 'Zingiberaceae', 'Zingiberoideae', NULL, 'Elettaria', 'cardamomum', 'Cardamom (Green)', 'Elettaria cardamomum', '(L.) Maton', 'LC', 'Spice', 'Ginger family; ginger, turmeric, cardamom', 7, '2026-06-26 15:47:47'),
    (153, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Magnoliidae', 'Laurales', 'Lauraceae', 'Lauroideae', NULL, 'Cinnamomum', 'verum', 'Cinnamon', 'Cinnamomum verum', 'J.Presl', 'LC', 'Spice', 'Laurel family; avocado, cinnamon, bay laurel', 250, '2026-06-26 15:47:47'),
    (154, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Myrtales', 'Myrtaceae', 'Myrtoideae', NULL, 'Syzygium', 'aromaticum', 'Clove', 'Syzygium aromaticum', '(L.) Merr. & L.M.Perry', 'LC', 'Spice', 'Myrtle family; includes guava, eucalyptus, clove', 1200, '2026-06-26 15:47:47'),
    (155, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Magnoliidae', 'Magnoliales', 'Myristicaceae', 'Myristicoideae', NULL, 'Myristica', 'fragrans', 'Nutmeg', 'Myristica fragrans', 'Houtt.', 'LC', 'Spice', '', 120, '2026-06-26 15:47:47'),
    (156, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Lilianae', 'Asparagales', 'Orchidaceae', 'Vanilloideae', NULL, 'Vanilla', 'planifolia', 'Vanilla', 'Vanilla planifolia', 'Andrews', 'VU', 'Spice', 'Orchid family; world''s largest plant family by species count', 110, '2026-06-26 15:47:47'),
    (157, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Apiales', 'Apiaceae', 'Apioideae', NULL, 'Cuminum', 'cyminum', 'Cumin', 'Cuminum cyminum', 'L.', 'LC', 'Spice', 'Carrot/Parsley family; umbellifers', 4, '2026-06-26 15:47:47'),
    (158, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Apiales', 'Apiaceae', 'Apioideae', NULL, 'Carum', 'carvi', 'Caraway', 'Carum carvi', 'L.', 'LC', 'Spice', 'Carrot/Parsley family; umbellifers', 30, '2026-06-26 15:47:47'),
    (159, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Apiales', 'Apiaceae', 'Apioideae', NULL, 'Trachyspermum', 'ammi', 'Ajwain (Carom)', 'Trachyspermum ammi', '(L.) Sprague', 'LC', 'Spice', 'Carrot/Parsley family; umbellifers', 15, '2026-06-26 15:47:47'),
    (160, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Magnoliidae', 'Austrobaileyales', 'Schisandraceae', 'Illicioideae', NULL, 'Illicium', 'verum', 'Star Anise', 'Illicium verum', 'Hook.f.', 'LC', 'Spice', '', 0, '2026-06-26 15:47:47'),
    (161, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Lilianae', 'Asparagales', 'Iridaceae', 'Iridoideae', NULL, 'Crocus', 'sativus', 'Saffron', 'Crocus sativus', 'L.', 'LC', 'Spice', '', 0, '2026-06-26 15:47:47'),
    (162, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Apiales', 'Apiaceae', 'Apioideae', NULL, 'Foeniculum', 'vulgare', 'Fennel', 'Foeniculum vulgare', 'Mill.', 'LC', 'Spice/Herb', 'Carrot/Parsley family; umbellifers', 1, '2026-06-26 15:47:47'),
    (163, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Apiales', 'Apiaceae', 'Apioideae', NULL, 'Anethum', 'graveolens', 'Dill', 'Anethum graveolens', 'L.', 'LC', 'Herb/Spice', 'Carrot/Parsley family; umbellifers', 2, '2026-06-26 15:47:47'),
    (164, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Sapindales', 'Meliaceae', 'Meliaceae', NULL, 'Azadirachta', 'indica', 'Neem', 'Azadirachta indica', 'A.Juss.', 'LC', 'Medicinal Tree', 'Mahogany family; includes neem, toon', 2, '2026-06-26 15:47:47'),
    (165, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Lamiales', 'Lamiaceae', 'Ocimeae', NULL, 'Ocimum', 'tenuiflorum', 'Tulsi (Holy Basil)', 'Ocimum tenuiflorum', 'L.', 'LC', 'Medicinal Herb', 'Mint/Sage family; aromatic herbs', 65, '2026-06-26 15:47:47'),
    (166, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Lamiales', 'Lamiaceae', 'Mentheae', NULL, 'Mentha', 'spicata', 'Mint (Spearmint)', 'Mentha spicata', 'L.', 'LC', 'Herb', 'Mint/Sage family; aromatic herbs', 18, '2026-06-26 15:47:47'),
    (167, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Lamiales', 'Lamiaceae', 'Mentheae', NULL, 'Mentha', 'piperita', 'Peppermint', 'Mentha x piperita', 'L.', 'LC', 'Herb', 'Mint/Sage family; aromatic herbs', 18, '2026-06-26 15:47:47'),
    (168, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Lamiales', 'Lamiaceae', 'Ocimeae', NULL, 'Ocimum', 'basilicum', 'Sweet Basil', 'Ocimum basilicum', 'L.', 'LC', 'Herb', 'Mint/Sage family; aromatic herbs', 65, '2026-06-26 15:47:47'),
    (169, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Lamiales', 'Lamiaceae', 'Mentheae', NULL, 'Salvia', 'rosmarinus', 'Rosemary', 'Salvia rosmarinus', 'Spenn.', 'LC', 'Herb', 'Mint/Sage family; aromatic herbs', 1000, '2026-06-26 15:47:47'),
    (170, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Lamiales', 'Lamiaceae', 'Mentheae', NULL, 'Thymus', 'vulgaris', 'Thyme', 'Thymus vulgaris', 'L.', 'LC', 'Herb', 'Mint/Sage family; aromatic herbs', 350, '2026-06-26 15:47:47'),
    (171, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Lamiales', 'Lamiaceae', 'Mentheae', NULL, 'Origanum', 'vulgare', 'Oregano', 'Origanum vulgare', 'L.', 'LC', 'Herb', 'Mint/Sage family; aromatic herbs', 44, '2026-06-26 15:47:47'),
    (172, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Lamiales', 'Lamiaceae', 'Ocimeae', NULL, 'Lavandula', 'angustifolia', 'Lavender', 'Lavandula angustifolia', 'Mill.', 'LC', 'Aromatic Herb', 'Mint/Sage family; aromatic herbs', 47, '2026-06-26 15:47:47'),
    (173, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Lamiales', 'Lamiaceae', 'Mentheae', NULL, 'Salvia', 'officinalis', 'Sage', 'Salvia officinalis', 'L.', 'LC', 'Herb', 'Mint/Sage family; aromatic herbs', 1000, '2026-06-26 15:47:47'),
    (174, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Apiales', 'Apiaceae', 'Apioideae', NULL, 'Petroselinum', 'crispum', 'Parsley', 'Petroselinum crispum', '(Mill.) Fuss', 'LC', 'Herb', 'Carrot/Parsley family; umbellifers', 0, '2026-06-26 15:47:47'),
    (175, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Lilianae', 'Asparagales', 'Xanthorrhoeaceae', 'Alooideae', NULL, 'Aloe', 'vera', 'Aloe Vera', 'Aloe vera', '(L.) Burm.f.', 'LC', 'Succulent/Medicinal', 'Aloe family (now classified here)', 550, '2026-06-26 15:47:47'),
    (176, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Solanales', 'Solanaceae', 'Solanoideae', NULL, 'Withania', 'somnifera', 'Ashwagandha', 'Withania somnifera', '(L.) Dunal', 'LC', 'Medicinal Herb', 'Nightshade family; tomato, potato, pepper, tobacco', 10, '2026-06-26 15:47:47'),
    (177, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Lamiales', 'Plantaginaceae', 'Gratioleae', NULL, 'Bacopa', 'monnieri', 'Brahmi (Water Hyssop)', 'Bacopa monnieri', '(L.) Wettst.', 'LC', 'Medicinal Herb', 'Plantain family; snapdragons, foxgloves', 70, '2026-06-26 15:47:47'),
    (178, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Ranunculidae', 'Ranunculales', 'Menispermaceae', 'Tinosporoideae', NULL, 'Tinospora', 'cordifolia', 'Giloy (Tinospora)', 'Tinospora cordifolia', '(Willd.) Miers', 'LC', 'Medicinal Climber', '', 32, '2026-06-26 15:47:47'),
    (179, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Poales', 'Poaceae', 'Panicoideae', NULL, 'Cymbopogon', 'citratus', 'Lemongrass', 'Cymbopogon citratus', '(DC.) Stapf', 'LC', 'Aromatic Herb', 'Grass family; cereals and grains - most economically important plant family', 55, '2026-06-26 15:47:47'),
    (180, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Poales', 'Poaceae', 'Panicoideae', NULL, 'Chrysopogon', 'zizanioides', 'Vetiver (Khus)', 'Chrysopogon zizanioides', '(L.) Roberty', 'LC', 'Aromatic Grass', 'Grass family; cereals and grains - most economically important plant family', 0, '2026-06-26 15:47:47'),
    (181, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Apiales', 'Apiaceae', 'Mackinlayoideae', NULL, 'Centella', 'asiatica', 'Gotu Kola', 'Centella asiatica', '(L.) Urb.', 'LC', 'Medicinal Herb', 'Carrot/Parsley family; umbellifers', 50, '2026-06-26 15:47:47'),
    (182, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Gentianales', 'Apocynaceae', 'Rauvolfioideae', NULL, 'Rauwolfia', 'serpentina', 'Sarpagandha (Indian Snakeroot)', 'Rauwolfia serpentina', '(L.) Benth. ex Kurz', 'EN', 'Medicinal Shrub', 'Dogbane family; includes oleander, periwinkle', 90, '2026-06-26 15:47:47'),
    (183, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Gentianales', 'Apocynaceae', 'Rauvolfioideae', NULL, 'Catharanthus', 'roseus', 'Periwinkle (Sadabahar)', 'Catharanthus roseus', '(L.) G.Don', 'LC', 'Medicinal Herb', 'Dogbane family; includes oleander, periwinkle', 8, '2026-06-26 15:47:47'),
    (184, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Lamiales', 'Acanthaceae', 'Andrographideae', NULL, 'Andrographis', 'paniculata', 'Andrographis (Kalmegh)', 'Andrographis paniculata', '(Burm.f.) Nees', 'LC', 'Medicinal Herb', '', 28, '2026-06-26 15:47:47'),
    (185, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Lamiales', 'Lamiaceae', 'Viticoideae', NULL, 'Tectona', 'grandis', 'Teak', 'Tectona grandis', 'L.f.', 'LC', 'Timber Tree', 'Mint/Sage family; aromatic herbs', 3, '2026-06-26 15:47:47'),
    (186, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Fabales', 'Fabaceae', 'Faboideae', NULL, 'Dalbergia', 'sissoo', 'Rosewood (Sheesham)', 'Dalbergia sissoo', 'DC.', 'NT', 'Timber Tree', 'Legume/Pea family; world''s second largest food plant family', 700, '2026-06-26 15:47:47'),
    (187, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Myrtales', 'Myrtaceae', 'Myrtoideae', NULL, 'Eucalyptus', 'globulus', 'Eucalyptus', 'Eucalyptus globulus', 'Labill.', 'LC', 'Timber/Medicinal Tree', 'Myrtle family; includes guava, eucalyptus, clove', 700, '2026-06-26 15:47:47'),
    (188, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Fabales', 'Fabaceae', 'Caesalpinioideae', NULL, 'Vachellia', 'nilotica', 'Babool (Acacia)', 'Vachellia nilotica', '(L.) P.J.H.Hurter & Mabb.', 'LC', 'Multipurpose Tree', 'Legume/Pea family; world''s second largest food plant family', 0, '2026-06-26 15:47:47'),
    (189, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Poales', 'Poaceae', 'Bambusoideae', NULL, 'Phyllostachys', 'edulis', 'Bamboo (Moso)', 'Phyllostachys edulis', '(Carrière) J.Houz.', 'LC', 'Bamboo', 'Grass family; cereals and grains - most economically important plant family', 0, '2026-06-26 15:47:47'),
    (190, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Poales', 'Poaceae', 'Bambusoideae', NULL, 'Dendrocalamus', 'strictus', 'Dendrocalamus (Giant Bamboo)', 'Dendrocalamus strictus', '(Roxb.) Nees', 'LC', 'Bamboo', 'Grass family; cereals and grains - most economically important plant family', 50, '2026-06-26 15:47:47'),
    (191, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Malvales', 'Dipterocarpaceae', 'Dipterocarpoideae', NULL, 'Shorea', 'robusta', 'Sal Tree', 'Shorea robusta', 'C.F.Gaertn.', 'NT', 'Forest Tree', '', 360, '2026-06-26 15:47:47'),
    (192, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Rosales', 'Moraceae', 'Moroideae', NULL, 'Ficus', 'religiosa', 'Peepal (Sacred Fig)', 'Ficus religiosa', 'L.', 'LC', 'Sacred Tree', 'Mulberry family; includes fig, breadfruit, jackfruit', 850, '2026-06-26 15:47:47'),
    (193, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Rosales', 'Moraceae', 'Moroideae', NULL, 'Ficus', 'benghalensis', 'Banyan Tree', 'Ficus benghalensis', 'L.', 'LC', 'Sacred Tree', 'Mulberry family; includes fig, breadfruit, jackfruit', 850, '2026-06-26 15:47:47'),
    (194, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Myrtales', 'Combretaceae', 'Combretoideae', NULL, 'Terminalia', 'arjuna', 'Arjuna Tree', 'Terminalia arjuna', '(Roxb. ex DC.) Wight & Arn.', 'LC', 'Medicinal Tree', 'Terminalia family; includes terminalia, arjuna, Indian almond', 0, '2026-06-26 15:47:47'),
    (195, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Sapindales', 'Meliaceae', 'Melioideae', NULL, 'Swietenia', 'mahagoni', 'Mahogany', 'Swietenia mahagoni', '(L.) Jacq.', 'EN', 'Timber Tree', 'Mahogany family; includes neem, toon', 4, '2026-06-26 15:47:47'),
    (196, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Malpighiales', 'Rhizophoraceae', 'Rhizophoroideae', NULL, 'Rhizophora', 'mangle', 'Mangrove (Red)', 'Rhizophora mangle', 'L.', 'LC', 'Mangrove', 'Mangrove family', 0, '2026-06-26 15:47:47'),
    (197, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Rosales', 'Rosaceae', 'Rosoideae', NULL, 'Rosa', 'indica', 'Rose', 'Rosa indica', 'L.', 'LC', 'Ornamental Flower', 'Rose family; includes apples, pears, cherries, plums, strawberries', 300, '2026-06-26 15:47:47'),
    (198, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Lamiales', 'Oleaceae', 'Oleoideae', NULL, 'Jasminum', 'sambac', 'Jasmine', 'Jasminum sambac', '(L.) Aiton', 'LC', 'Ornamental Flower', 'Olive family; olives, jasmine, ash trees', 200, '2026-06-26 15:47:47'),
    (199, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Malvales', 'Malvaceae', 'Malvoideae', NULL, 'Hibiscus', 'rosa-sinensis', 'Hibiscus', 'Hibiscus rosa-sinensis', 'L.', 'LC', 'Ornamental Flower', 'Mallow family; cotton, hibiscus, cacao, durian', 679, '2026-06-26 15:47:47'),
    (200, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Proteidae', 'Proteales', 'Nelumbonaceae', 'Nelumbonoideae', NULL, 'Nelumbo', 'nucifera', 'Lotus', 'Nelumbo nucifera', 'Gaertn.', 'LC', 'Aquatic Flower', 'Lotus family', 2, '2026-06-26 15:47:47');
INSERT INTO taxonomy_full (id, kingdom, subkingdom, division, subdivision, class_name, subclass, order_name, family_name, subfamily, tribe, genus, species, common_name, botanical_name, author_citation, iucn_status, category, family_description, genera_species_count, created_at) VALUES
    (201, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Asterales', 'Asteraceae', 'Tagetinae', NULL, 'Tagetes', 'erecta', 'Marigold', 'Tagetes erecta', 'L.', 'LC', 'Ornamental Flower', 'Daisy/Composite family; world''s largest flowering plant family', 56, '2026-06-26 15:47:47'),
    (202, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Asterales', 'Asteraceae', 'Anthemideae', NULL, 'Chrysanthemum', 'morifolium', 'Chrysanthemum', 'Chrysanthemum morifolium', 'Ramat.', 'LC', 'Ornamental Flower', 'Daisy/Composite family; world''s largest flowering plant family', 40, '2026-06-26 15:47:47'),
    (203, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Caryophyllidae', 'Caryophyllales', 'Caryophyllaceae', 'Caryophylloideae', NULL, 'Dianthus', 'caryophyllus', 'Carnation', 'Dianthus caryophyllus', 'L.', 'LC', 'Ornamental Flower', '', 300, '2026-06-26 15:47:47'),
    (204, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Caryophyllidae', 'Caryophyllales', 'Nyctaginaceae', 'Bougainvilleoideae', NULL, 'Bougainvillea', 'spectabilis', 'Bougainvillea', 'Bougainvillea spectabilis', 'Willd.', 'LC', 'Ornamental Climber', '', 18, '2026-06-26 15:47:47'),
    (205, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Asterales', 'Asteraceae', 'Coreopsideae', NULL, 'Dahlia', 'pinnata', 'Dahlia', 'Dahlia pinnata', 'Cav.', 'LC', 'Ornamental Flower', 'Daisy/Composite family; world''s largest flowering plant family', 42, '2026-06-26 15:47:47'),
    (206, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Lilianae', 'Liliales', 'Liliaceae', 'Lilioideae', NULL, 'Tulipa', 'gesneriana', 'Tulip', 'Tulipa gesneriana', 'L.', 'LC', 'Ornamental Flower', 'True lily family', 109, '2026-06-26 15:47:47'),
    (207, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Lilianae', 'Asparagales', 'Orchidaceae', 'Epidendroideae', NULL, 'Phalaenopsis', 'amabilis', 'Orchid (Phalaenopsis)', 'Phalaenopsis amabilis', '(L.) Blume', 'VU', 'Ornamental Flower', 'Orchid family; world''s largest plant family by species count', 0, '2026-06-26 15:47:47'),
    (208, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Lilianae', 'Liliales', 'Liliaceae', 'Lilioideae', NULL, 'Lilium', 'longiflorum', 'Lily (Easter)', 'Lilium longiflorum', 'Thunb.', 'LC', 'Ornamental Flower', 'True lily family', 111, '2026-06-26 15:47:47'),
    (209, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Asteridae', 'Asterales', 'Asteraceae', 'Heliantheae', NULL, 'Zinnia', 'elegans', 'Zinnia', 'Zinnia elegans', 'Jacq.', 'LC', 'Ornamental Flower', 'Daisy/Composite family; world''s largest flowering plant family', 22, '2026-06-26 15:47:47'),
    (210, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Commelinidae', 'Commelinales', 'Pontederiaceae', 'Pontederioideae', NULL, 'Eichhornia', 'crassipes', 'Water Hyacinth', 'Eichhornia crassipes', '(Mart.) Solms', 'LC', 'Aquatic/Invasive', '', 7, '2026-06-26 15:47:47'),
    (211, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Caryophyllidae', 'Caryophyllales', 'Droseraceae', 'Droseridae', NULL, 'Dionaea', 'muscipula', 'Venus Flytrap', 'Dionaea muscipula', 'Sol. ex J.Ellis', 'VU', 'Carnivorous Plant', 'Sundew family; carnivorous plants', 0, '2026-06-26 15:47:47'),
    (212, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Caryophyllidae', 'Caryophyllales', 'Droseraceae', 'Droseridae', NULL, 'Drosera', 'rotundifolia', 'Sundew', 'Drosera rotundifolia', 'L.', 'LC', 'Carnivorous Plant', 'Sundew family; carnivorous plants', 0, '2026-06-26 15:47:47'),
    (213, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Caryophyllidae', 'Caryophyllales', 'Nepenthaceae', 'Nepentheae', NULL, 'Nepenthes', 'rajah', 'Pitcher Plant', 'Nepenthes rajah', 'Hook.f.', 'EN', 'Carnivorous Plant', 'Tropical pitcher plant family', 0, '2026-06-26 15:47:47'),
    (214, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Caryophyllidae', 'Caryophyllales', 'Cactaceae', 'Cactoideae', NULL, 'Opuntia', 'ficus-indica', 'Prickly Pear Cactus', 'Opuntia ficus-indica', '(L.) Mill.', 'LC', 'Cactus/Fruit', 'Cactus family; succulent xerophytes', 200, '2026-06-26 15:47:47'),
    (215, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Liliopsida', 'Lilianae', 'Asparagales', 'Asparagaceae', 'Agavoideae', NULL, 'Agave', 'americana', 'Agave (Century Plant)', 'Agave americana', 'L.', 'LC', 'Succulent', 'Asparagus family; includes agave, yucca', 208, '2026-06-26 15:47:47'),
    (216, 'Plantae', 'Viridaeplantae', 'Polypodiophyta', NULL, 'Polypodiopsida', 'Polypodiidae', 'Dennstaedtiales', 'Dennstaedtiaceae', 'Dennstaedtioideae', NULL, 'Pteridium', 'aquilinum', 'Common Bracken Fern', 'Pteridium aquilinum', '(L.) Kuhn', 'LC', 'Fern', '', 0, '2026-06-26 15:47:47'),
    (217, 'Plantae', 'Viridaeplantae', 'Bryophyta', NULL, 'Sphagnopsida', 'Sphagnidae', 'Sphagnales', 'Sphagnaceae', 'Sphagnoideae', NULL, 'Sphagnum', 'palustre', 'Peat Moss', 'Sphagnum palustre', 'L.', 'LC', 'Moss/Bryophyte', 'Peat moss family', 0, '2026-06-26 15:47:47'),
    (218, 'Plantae', 'Cyanobacteria', 'Cyanophyta', NULL, 'Cyanophyceae', 'Oscillatoriophycideae', 'Oscillatoriales', 'Microcoleaceae', 'Microcoleaceae', NULL, 'Arthrospira', 'platensis', 'Spirulina (Blue-Green Algae)', 'Arthrospira platensis', '(Nordstedt) Gomont', 'LC', 'Algae/Superfood', '', 0, '2026-06-26 15:47:47'),
    (219, 'Plantae', 'Chromalveolata', 'Phaeophyta', NULL, 'Phaeophyceae', 'Fucidae', 'Laminariales', 'Laminariaceae', 'Laminarioideae', NULL, 'Saccharina', 'latissima', 'Kelp Seaweed', 'Saccharina latissima', '(L.) C.E.Lane, C.Mayes, Druehl & G.W.Saunders', 'LC', 'Seaweed/Algae', '', 0, '2026-06-26 15:47:47'),
    (220, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Fabales', 'Fabaceae', 'Faboideae', NULL, 'Sesbania', 'bispinosa', 'Sesbania (Dhaincha)', 'Sesbania bispinosa', '(Jacq.) W.Wight', 'LC', 'Green Manure', 'Legume/Pea family; world''s second largest food plant family', 60, '2026-06-26 15:47:47'),
    (221, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Fabales', 'Fabaceae', 'Faboideae', NULL, 'Crotalaria', 'juncea', 'Sunn Hemp', 'Crotalaria juncea', 'L.', 'LC', 'Green Manure/Fiber', 'Legume/Pea family; world''s second largest food plant family', 0, '2026-06-26 15:47:47'),
    (222, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Fabales', 'Fabaceae', 'Faboideae', NULL, 'Mucuna', 'pruriens', 'Velvet Bean (Mucuna)', 'Mucuna pruriens', '(L.) DC.', 'LC', 'Cover Crop/Medicinal', 'Legume/Pea family; world''s second largest food plant family', 105, '2026-06-26 15:47:47'),
    (223, 'Plantae', 'Viridaeplantae', 'Tracheophyta', 'Spermatophytina', 'Magnoliopsida', 'Rosidae', 'Fabales', 'Fabaceae', 'Faboideae', NULL, 'Gliricidia', 'sepium', 'Gliricidia', 'Gliricidia sepium', '(Jacq.) Kunth ex Walp.', 'LC', 'Agroforestry/Fodder', 'Legume/Pea family; world''s second largest food plant family', 0, '2026-06-26 15:47:47');

DROP TABLE IF EXISTS plant_diseases CASCADE;
CREATE TABLE plant_diseases (
    id INTEGER PRIMARY KEY NOT NULL,
    disease_name VARCHAR(200) NOT NULL,
    pathogen_name VARCHAR(300) NULL,
    disease_type VARCHAR(100) NULL,
    affected_plant VARCHAR(200) NULL,
    host_range VARCHAR(255) NULL,
    risk_level VARCHAR(50) NULL,
    economic_impact VARCHAR(255) NULL,
    geographic_distribution VARCHAR(255) NULL,
    favorable_conditions VARCHAR(255) NULL,
    early_symptoms VARCHAR(255) NULL,
    late_symptoms VARCHAR(255) NULL,
    affected_parts VARCHAR(300) NULL,
    disease_cycle VARCHAR(255) NULL,
    incubation_period VARCHAR(100) NULL,
    organic_treatment VARCHAR(255) NULL,
    chemical_treatment VARCHAR(255) NULL,
    biological_treatment VARCHAR(255) NULL,
    preventive_measures VARCHAR(255) NULL,
    application_frequency VARCHAR(200) NULL,
    recovery_time VARCHAR(200) NULL,
    phi_days INTEGER NULL,
    created_at TIMESTAMP NULL
);

-- Data for plant_diseases (33 rows)
INSERT INTO plant_diseases (id, disease_name, pathogen_name, disease_type, affected_plant, host_range, risk_level, economic_impact, geographic_distribution, favorable_conditions, early_symptoms, late_symptoms, affected_parts, disease_cycle, incubation_period, organic_treatment, chemical_treatment, biological_treatment, preventive_measures, application_frequency, recovery_time, phi_days, created_at) VALUES
    (1, 'Early Blight', 'Alternaria solani', 'Fungal', 'Tomato', 'Tomato, Potato, Eggplant', 'Medium', 'Reduces yield by 30-50% in warm humid conditions. Major yield loss in unmanaged fields.', 'Worldwide', 'Warm temperatures (24-29°C), High humidity (>90%), Wet foliage', 'Small, dark brown circular spots with concentric rings (target board pattern) on older lower leaves', 'Leaf yellowing, premature leaf drop, dark sunken lesions at stem-ends of fruit, stem collar rot', 'Leaves, Stem, Fruit', 'Overwinters in infected plant debris. Conidia spread by wind and rain splash. Infection requires 2-3 hours of wet leaf surface.', '2-3 days', 'Neem oil (4ml/L + 2ml soap), Copper oxychloride 50% WP (3g/L), Trichoderma harzianum soil drench, Baking soda spray (5g/L)', 'Mancozeb 75% WP (2g/L), Azoxystrobin 23% SC (1ml/L), Chlorothalonil 75% WP (2g/L), Propiconazole 25% EC (1ml/L)', 'Trichoderma viride, Bacillus subtilis strains QST713, Pseudomonas fluorescens', 'Use certified disease-free seeds, crop rotation (3 years), remove infected debris, avoid overhead irrigation, stake plants for air circulation', 'Every 7-10 days in wet weather', '10-14 days with treatment', 7, '2026-06-26 15:47:47'),
    (2, 'Late Blight', 'Phytophthora infestans', 'Oomycete', 'Tomato', 'Tomato, Potato', 'Critical', 'Can destroy entire field in 5-7 days. Caused the Irish Potato Famine (1845-49).', 'Worldwide, especially cool humid climates', 'Cool temperature (10-20°C), High humidity (>90%), Rain, dew', 'Water-soaked irregular grayish-green patches on leaves, usually starting from leaf tips and edges', 'Fuzzy white sporulating lesions on underside of leaves in humid conditions, greasy dark green-black patches on fruit, entire plant collapse with putrid smell', 'Leaves, Stems, Fruit', 'Sporangia spread by wind and rain. Sexual oospores persist in soil. Highly explosive under wet cool conditions.', '3-5 days', 'Copper hydroxide (3g/L) as protective spray, Bordeaux mixture (1%), maintain dry conditions', 'Metalaxyl-M + Mancozeb (Ridomil Gold) 2.5g/L, Cymoxanil + Famoxadone 0.5g/L, Dimethomorph 0.5g/L', 'Bacillus subtilis (Serenade), Streptomyces lydicus', 'Plant resistant varieties, ensure good drainage, avoid overhead irrigation, scout regularly during cool wet weather, destroy volunteer plants', 'Every 5-7 days during epidemic periods', '7-10 days (preventive focus; infected plants rarely recover)', 7, '2026-06-26 15:47:47'),
    (3, 'Tomato Yellow Leaf Curl Virus (TYLCV)', 'Tomato yellow leaf curl virus', 'Viral', 'Tomato', 'Tomato, Pepper, Bean, Eggplant', 'High', 'Can cause 100% yield loss in unmanaged greenhouses. Major problem in warm regions.', 'Mediterranean, Middle East, South Asia, Americas, Sub-Saharan Africa', 'High whitefly populations, temperatures above 25°C', 'Upward and inward curling of leaflets, yellowing at leaf margins', 'Severe stunting, complete yellowing, flower drop, no fruit set or deformed fruits', 'Leaves, Growing Tips, Fruit', 'Transmitted by whitefly (Bemisia tabaci) in a persistent circulative manner. No seed transmission.', '14-21 days', 'No cure once infected; control whitefly vector with neem oil, yellow sticky traps, reflective mulch', 'Imidacloprid or Thiamethoxam for whitefly control. Mineral oil sprays to reduce whitefly transmission', 'Encarsia formosa parasitoid, Beauveria bassiana for whiteflies', 'Plant TYLCV-resistant varieties, use insect-proof netting in nursery, roguing infected plants immediately, control whiteflies', 'Whitefly control every 7-10 days', 'No recovery; remove infected plants', NULL, '2026-06-26 15:47:47'),
    (4, 'Fusarium Wilt', 'Fusarium oxysporum f. sp. lycopersici', 'Fungal', 'Tomato', 'Tomato (host-specific)', 'High', 'Major cause of tomato field losses, especially in sandy soils.', 'Worldwide', 'Warm soils (25-30°C), light sandy soils, acid soils', 'Yellowing and wilting of lower leaves starting on one side of the plant, often one branch first', 'Complete wilting and death, brown internal vascular discoloration visible when stem is cut crosswise', 'Roots, Stem (vascular), Leaves', 'Soil-borne pathogen. Survives for years in soil as chlamydospores. Enters through roots, grows in xylem blocking water flow.', '7-14 days', 'Trichoderma harzianum soil treatment, Solarization (clear polyethylene film over moist soil for 4-6 weeks)', 'No effective chemical cure; soil fumigation with Metam sodium before planting as preventive', 'Trichoderma viride, Pseudomonas fluorescens root dip, Bacillus subtilis', 'Plant resistant varieties (race-specific), crop rotation (4+ years), avoid wounding roots, soil solarization', 'Soil treatments at planting', 'No recovery; remove infected plants', NULL, '2026-06-26 15:47:47'),
    (5, 'Bacterial Wilt', 'Ralstonia solanacearum', 'Bacterial', 'Tomato', 'Tomato, Potato, Pepper, Eggplant, Banana, Tobacco, Ginger', 'Critical', 'One of the most destructive soilborne diseases worldwide; can destroy entire plantations.', 'Tropical, subtropical, warm temperate regions worldwide', 'High temperatures (28-35°C), high soil moisture, damaged roots', 'Sudden wilting of top leaves during hottest part of the day, recovery at night', 'Permanent wilting even at night, water-soaked stem interior, oozing of bacterial slime (white to gray) from cut stems dipped in water', 'Entire plant, Vascular system', 'Spreads through soil, water, infected plant material. Enters through roots. Multiplies in xylem.', '3-7 days', 'No effective cure. Copper-based bactericides as weak suppressants', 'No effective chemical treatment available', 'Bacillus subtilis and Pseudomonas fluorescens as biological suppressants (preventive only)', 'Plant resistant varieties, crop rotation (minimum 3 years), soil solarization, avoid waterlogging, remove infected plants and soil, use clean tools', 'Preventive only', 'No recovery; remove infected plants immediately', NULL, '2026-06-26 15:47:47'),
    (6, 'Septoria Leaf Spot', 'Septoria lycopersici', 'Fungal', 'Tomato', 'Tomato, Potato (limited)', 'Medium', 'Severe defoliation, reduces photosynthesis, leads to sunscald on fruit. Up to 40% yield loss.', 'Worldwide, common in humid temperate regions', 'Wet weather, temperatures 20-25°C, leaf wetness > 4 hours', 'Small, circular water-soaked spots on lower leaves with dark brown margins and lighter gray-white centers with tiny black dots (pycnidia)', 'Extensive defoliation starting from bottom of plant upward, sun-scalded fruits exposed to direct sun', 'Leaves (lower first)', 'Overwinters in infected debris. Conidia splash-spread by rain. Infection requires wet leaf surface.', '5 days', 'Copper oxychloride 50% WP (3g/L), neem oil spray, remove infected lower leaves', 'Chlorothalonil (2g/L), Mancozeb (2g/L), Azoxystrobin (0.5ml/L)', 'Bacillus subtilis', 'Crop rotation, remove infected plant debris, avoid overhead irrigation, stake and prune for air circulation', 'Every 10-14 days', '14-21 days', 7, '2026-06-26 15:47:47'),
    (7, 'Powdery Mildew (Tomato)', 'Leveillula taurica', 'Fungal', 'Tomato', 'Tomato, Pepper, Eggplant', 'Low', 'Reduces yield by 10-20% through photosynthesis reduction', 'Dry, warm regions worldwide', 'Low humidity (50-70%), temperatures 18-28°C, common in greenhouses', 'Pale yellow spots on upper leaf surface, white powdery growth visible on underside', 'Entire leaf covered with white powder, premature defoliation', 'Leaves', 'Obligate parasite; spreads by airborne conidia. Internal mycelium attacks from inside leaf.', '5-7 days', 'Wettable sulfur (3g/L), potassium bicarbonate (5g/L), neem oil, diluted milk (1:9)', 'Hexaconazole (1ml/L), Propiconazole (1ml/L), Tebuconazole (1ml/L)', 'Ampelomyces quisqualis, Bacillus subtilis', 'Good air circulation, avoid dense planting, resistant varieties', 'Every 7-10 days', '7-14 days', 14, '2026-06-26 15:47:47'),
    (8, 'Blossom End Rot', 'Calcium deficiency (Physiological)', 'Physiological Disorder', 'Tomato', 'Tomato, Pepper, Eggplant, Watermelon, Squash', 'Medium', 'Can render 25-50% of fruits unmarketable during severe calcium stress.', 'Worldwide', 'Irregular watering, drought stress, soil pH imbalance, excess nitrogen or potassium', 'Light brown water-soaked area at blossom end of green fruit', 'Expanding dark brown to black leathery sunken patch at fruit base, secondary fungal colonization', 'Fruit (blossom end)', 'Not infectious; caused by calcium translocation failure due to irregular water stress.', 'Appears 6-8 weeks after planting', 'Foliar calcium chloride spray (4g/L), consistent irrigation, mulching, agricultural lime in soil', 'Calcium nitrate foliar spray (2g/L), drip application of calcium chelate', 'Not applicable', 'Consistent irrigation schedule, mulch to retain soil moisture, soil pH 6.2-6.8, avoid excess ammonium nitrogen', 'Calcium spray every 7-10 days when fruits are forming', 'Affected fruits do not recover; new fruits will be healthy with correction', NULL, '2026-06-26 15:47:47'),
    (9, 'Root Knot Nematode', 'Meloidogyne incognita, M. javanica', 'Nematode', 'Tomato', 'Tomato, Pepper, Cucumber, Beans, and 2,000+ other plant species', 'High', 'Up to 80% yield loss in heavily infested sandy soils.', 'Tropical and subtropical regions worldwide', 'Sandy soils, temperatures 25-30°C, high soil moisture', 'Wilting during hot hours, poor plant vigor, chlorosis resembling nutrient deficiency', 'Typical galls (root knots) on roots when pulled, stunted growth, reduced yield', 'Roots', 'Females lay eggs in soil. Juveniles penetrate roots, induce gall formation. Multiple generations per season.', '21-30 days to complete one generation', 'Marigold intercropping (Tagetes sp.), neem cake soil application, Paecilomyces lilacinus, Pochonia chlamydosporia', 'Carbofuran 3G (33kg/ha soil application), Ethoprophos 10G granules, Oxamyl', 'Purpureocillium lilacinum, Trichoderma harzianum, Bacillus firmus', 'Crop rotation with non-host crops (maize, cereals), soil solarization, use resistant varieties (Mi-gene)', 'Soil treatment at planting and 30 DAS', 'Suppression over 1-2 seasons', 60, '2026-06-26 15:47:47'),
    (10, 'Rice Blast', 'Pyricularia oryzae (Magnaporthe oryzae)', 'Fungal', 'Rice', 'Rice, Barley, Wheat, Foxtail millet', 'Critical', 'Most destructive rice disease globally. Causes 10-30% annual losses; can cause up to 100% loss.', '85+ countries globally', 'Night temperatures 17-22°C, leaf wetness > 10 hours, high humidity, excess nitrogen', 'Spindle-shaped (diamond) lesions on leaves with gray-white center and dark brown to reddish-brown margins', 'Neck rot: lesion at panicle neck causes the head to break and hang down (Neck Blast). Grain blast: empty chaffy grains. Node blast: dark lesions at stem nodes.', 'Leaves, Nodes, Panicle Neck, Grains', 'Conidia spread by wind; infection requires 10+ hours leaf wetness. Overwinters in infected debris, volunteer rice, and alternate hosts.', '4-5 days at 25°C', 'Spray Pseudomonas fluorescens (1% w/v), seed treatment with Trichoderma, avoid excess nitrogen', 'Tricyclazole 75% WP (0.6g/L), Isoprothiolane 40% EC (1.5ml/L), Kasugamycin 3% SL (1.5ml/L), Azoxystrobin', 'Pseudomonas fluorescens, Bacillus subtilis, Trichoderma harzianum', 'Use blast-resistant varieties (BPT 5204, Swarna Sub1), balanced N fertilization, wider spacing for air circulation, destroy stubble', 'At tillering and booting stages; repeat at 10-14 day intervals if disease pressure continues', '12-15 days with systemic fungicide', 14, '2026-06-26 15:47:47'),
    (11, 'Bacterial Leaf Blight (BLB)', 'Xanthomonas oryzae pv. oryzae', 'Bacterial', 'Rice', 'Rice (primary), wild Oryza species', 'High', 'Causes 20-30% yield loss in susceptible varieties; up to 70% in severe epidemics.', 'Asia, West Africa, Australia', 'High temperature (25-34°C), high humidity, wind, flooding, heavy nitrogen fertilization', 'Water-soaked to yellowish stripes along leaf margins, turning white to grayish, ''Kresek'' phase in young seedlings (complete wilting)', 'Milky, opaque bacterial exudate (dried beads) visible in morning on leaf tips, pale yellow ''straw'' leaves, withered diseased panicles', 'Leaves, growing tips', 'Enters through water pores (hydathodes) and wounds. Spread by rain splash, floodwater, and wind. Overwinters in infected stubble and wild rice.', '7-14 days', 'Drain fields; copper hydroxide (2g/L) as weak bactericide spray', 'Streptomycin + Tetracycline combination (limited effectiveness); Copper oxychloride preventively', 'Pseudomonas fluorescens (preventive soil and foliar treatment)', 'Plant resistant varieties (IR64, Swarna), avoid excessive nitrogen, drain infected fields, destroy stubble', 'Copper sprays every 10 days in high-risk periods', 'Suppression; no cure for infected plants', NULL, '2026-06-26 15:47:47'),
    (12, 'Sheath Blight', 'Rhizoctonia solani AG1-IA', 'Fungal', 'Rice', 'Rice, Maize, Soybean, Sugarcane, and many other crops', 'High', 'Second most important rice disease after blast. Causes 20-50% yield loss in high-density plantings.', 'Worldwide, especially tropical Asia', 'High humidity, temperatures 28-32°C, dense canopy, high nitrogen, standing water', 'Oval to elliptical greenish-gray lesions with white-gray interior and brownish border on leaf sheaths at water level', 'Lesions coalesce and extend to upper leaves, white mycelial growth and brown sclerotia visible, complete sheath and leaf death', 'Leaf sheaths (primarily), Leaves, Stem', 'Survives as sclerotia in soil and crop debris. Sclerotia float to base of plants and initiate infection. Spreads upward under humid conditions.', '3-4 days', 'Trichoderma harzianum or T. viride soil application (2.5 kg/ha), Pseudomonas fluorescens spray', 'Hexaconazole 5% EC (1ml/L), Propiconazole 25% EC (1ml/L), Validamycin 3% L (2ml/L), Carbendazim (1g/L)', 'Trichoderma harzianum, Bacillus subtilis', 'Reduce plant density, lower nitrogen, drain standing water, use resistant varieties', 'At tillering, repeat at 10-14 day intervals in humid conditions', '14-21 days', 14, '2026-06-26 15:47:47'),
    (13, 'Brown Spot', 'Helminthosporium oryzae (Bipolaris oryzae)', 'Fungal', 'Rice', 'Rice, Corn, Sorghum, Sugarcane', 'Medium', 'Contributed to Great Bengal Famine (1943). Causes 5-45% yield loss.', 'Worldwide, worse in nutrient-deficient soils', 'Temperatures 25-30°C, high humidity, nutrient-deficient (especially potassium) soils', 'Small, oval to circular spots on leaves with yellow halo; dark brown margins and lighter centers', 'Spots enlarge to typical oval brown spots, leaves yellow and die; glume discoloration leading to pecky rice', 'Leaves, Grain (glumes)', 'Seed-borne; spreads by conidia through wind and rain. Survives in infected seeds and crop debris.', '5-6 days', 'Trichoderma seed treatment, adequate potassium nutrition', 'Mancozeb 75% WP (2g/L), Propiconazole 25% EC (1ml/L), Iprodione (1.5g/L)', 'Trichoderma viride seed treatment', 'Treat seeds with fungicide, correct soil nutrition (especially K and Si), use certified seeds, crop rotation', '2-3 sprays during crop season', '10-14 days', 14, '2026-06-26 15:47:47'),
    (14, 'False Smut', 'Ustilaginoidea virens', 'Fungal', 'Rice', 'Rice', 'Low', 'Reduces grain quality and weight by 2-15%. Produces toxic ustiloxins.', 'All rice-growing areas, especially with high humidity at flowering', 'High humidity and rainfall during heading and flowering stage, temperatures 25-35°C', 'Individual spikelets converted to small velvet-like greenish balls', 'Balls enlarge to 10mm diameter, becoming orange-yellow then olive-green with black powdery spores, scattered through panicle', 'Grain/Spikelets', 'Infection during flowering stage. Spores survive in soil and air. Spreads by wind.', 'Infection at flowering, visible at maturity', 'Propiconazole-based sprays at booting stage', 'Propiconazole 25% EC (1ml/L) or Azoxystrobin at booting stage', 'No effective biological control', 'Spray preventive fungicide at booting stage, avoid late planting, balanced nutrition', 'One spray at booting stage', 'Prevention only; affected grains cannot be treated', 21, '2026-06-26 15:47:47'),
    (15, 'Stripe Rust (Yellow Rust)', 'Puccinia striiformis f. sp. tritici', 'Fungal', 'Wheat', 'Wheat, Barley, Triticale, wild grasses', 'High', 'Can cause 70% yield loss. Major rust affecting wheat in cool humid regions.', 'Worldwide, especially in cooler regions', 'Cool temperatures (7-15°C), morning dew, high humidity', 'Stripe of yellow-orange uredia arranged in rows along leaf veins on upper leaf surface', 'Extensive yellowing of leaves, black teliospores in stripes, reduced grain fill, shriveled kernels', 'Leaves, Leaf sheaths, Glumes', 'Obligate parasite; spreads by wind-borne urediniospores. Overwinters on living green tissue. Long-distance spread by wind.', '9-10 days at optimal temperature', 'Wettable sulfur preventively; no effective organic cure', 'Propiconazole 25% EC (1ml/L), Tebuconazole 250 EW (1ml/L), Azoxystrobin + Propiconazole', 'Limited; Trichoderma as preventive', 'Plant resistant varieties (HD-3226, WH1105), timely sowing to escape high-risk period, prophylactic fungicide at flag leaf stage', 'One spray at flag leaf + repeat 14 days later if severe', '10-14 days', 21, '2026-06-26 15:47:47'),
    (16, 'Stem Rust (Black Rust)', 'Puccinia graminis f. sp. tritici', 'Fungal', 'Wheat', 'Wheat, Barley, Rye, many grasses', 'Critical', 'Ug99 race caused international alarm in 2000s; can cause near-total crop failure.', 'Worldwide', 'Warm temperatures (18-30°C), high humidity, dew', 'Brick-red oval to elongated blisters (pustules) on stems and leaves that rupture releasing reddish-brown powdery spores', 'Black teliospore pustules in late season, lodging of stems, shriveled grain', 'Stems, Leaves, Leaf sheaths, Glumes', 'Two-host cycle: Puccinia graminis requires barberry (Berberis sp.) as alternate host for sexual recombination. Urediniospores spread by wind.', '8-14 days', 'Wettable sulfur; remove barberry bushes from fields', 'Propiconazole 25% EC (1ml/L), Tebuconazole (1ml/L), at first sign of infection', 'No effective biological control for field use', 'Rust-resistant varieties, eradicate barberry, prophylactic fungicide in Ug99-risk areas', 'At first sign, repeat after 14 days', '10-14 days', 21, '2026-06-26 15:47:47'),
    (17, 'Loose Smut', 'Ustilago tritici', 'Fungal', 'Wheat', 'Wheat', 'Medium', 'Causes 5-30% yield loss. Entire head is replaced by black smut mass.', 'Worldwide', 'Cool moist conditions during flowering, moderate temperatures', 'Diseased plants emerge earlier; infected ear with black spore mass instead of grain', 'Complete head replaced by black teliospore mass that disperses, leaving bare rachis', 'Ear/Panicle', 'Seed-borne; mycelium is dormant in seed embryo. Infection occurs at flowering. No external symptoms until next season.', 'Entire growing season (symptom appears at heading of next crop)', 'Hot water seed treatment (52°C for 10 minutes)', 'Carboxin + Thiram seed treatment (2g/kg seed), Tebuconazole seed treatment', 'Trichoderma viride seed treatment', 'Use certified smut-free seeds, systemic seed treatment fungicides, plant resistant varieties', 'Seed treatment before sowing', 'Not applicable (seed treatment prevents disease)', NULL, '2026-06-26 15:47:47'),
    (18, 'Powdery Mildew (Wheat)', 'Blumeria graminis f. sp. tritici', 'Fungal', 'Wheat', 'Wheat (host-specific)', 'Medium', 'Causes 5-40% yield loss in cool humid conditions.', 'Worldwide, especially cool humid regions', 'Cool temperatures (15-22°C), moderate humidity, dense crop canopy', 'White fluffy powdery patches on upper leaf surface of lower leaves', 'White-gray coating on all green parts, yellowing and drying of leaves, cleistothecia (black dots) visible in old patches', 'Leaves, Stems, Leaf sheaths', 'Obligate parasite; spreads by airborne conidia. Overwinters as cleistothecia on straw.', '5-7 days', 'Wettable sulfur (3g/L), potassium bicarbonate', 'Propiconazole 25% EC (1ml/L), Triadimefon 25% WP (1g/L), Azoxystrobin', 'Ampelomyces quisqualis', 'Resistant varieties, avoid dense planting, balanced nitrogen, timely fungicide sprays', 'At first signs, repeat after 14 days', '10-14 days', 21, '2026-06-26 15:47:47'),
    (19, 'Northern Corn Leaf Blight (NCLB)', 'Exserohilum turcicum (Setosphaeria turcica)', 'Fungal', 'Maize', 'Maize, Sorghum, Sudan grass', 'High', 'Causes 10-50% yield loss. Major foliar disease in warm humid maize regions.', 'Worldwide in humid maize-growing regions', 'Temperatures 18-27°C, prolonged dew periods, high humidity', 'Long (5-15cm) elliptical tan to grayish-green lesions with wavy margins on lower leaves', 'Extensive leaf blighting from bottom of plant upward, dark olive-green spore mass on lesions in humid conditions', 'Leaves', 'Overwinters in infected crop debris. Conidia spread by wind and rain. Multiple infection cycles per season.', '7-12 days', 'Copper-based fungicides preventively', 'Azoxystrobin + Propiconazole (Quilt Xcel 1L/ha), Propiconazole alone (1ml/L)', 'Bacillus amyloliquefaciens', 'Resistant hybrids, crop rotation, remove infected debris, timely planting', 'At VT/R1 stage (tasseling) preventively; repeat if disease pressure', '14-21 days', 21, '2026-06-26 15:47:47'),
    (20, 'Maize Lethal Necrosis (MLN)', 'Maize chlorotic mottle virus (MCMV) + Potyviruses', 'Viral', 'Maize', 'Maize, Sorghum, some grasses', 'Critical', 'Can cause 100% yield loss. Emerging disease devastating East African maize belts since 2011.', 'East Africa (Kenya, Uganda, Tanzania, Ethiopia), Asia (China, Thailand)', 'High thrips, aphid, beetle populations; monoculture farming systems', 'Chlorotic (yellow) streaks and mottling on younger leaves; pale green to yellow leaf discoloration', 'Complete necrosis of all leaves from leaf tip, brown papery leaves, ear rot, premature death', 'All plant parts, especially leaves and ears', 'MCMV transmitted by thrips, beetles, aphids; SCMV/WSMV transmitted by aphids. Synergistic interaction causes lethal necrosis.', '14-21 days', 'No cure; control insect vectors with neem oil, reflective mulch', 'No direct treatment; insecticides for vector control (Imidacloprid, Thiamethoxam)', 'No effective biological treatment', 'Plant MLN-tolerant/resistant varieties, control thrips and aphids, crop rotation, early planting, remove infected plants', 'Vector control every 7-10 days in high-pressure periods', 'No recovery; remove infected plants', NULL, '2026-06-26 15:47:47'),
    (21, 'Gray Leaf Spot', 'Cercospora zeae-maydis', 'Fungal', 'Maize', 'Maize', 'High', 'Major disease in high-elevation maize areas. 10-50% yield reduction.', 'Worldwide, especially Africa, USA Corn Belt, Latin America', 'Warm humid weather, extended leaf wetness, minimum tillage, dense canopy', 'Small, irregular tan spots with yellow halos, mainly on lower leaves', 'Elongated, rectangular, grayish-tan lesions limited by leaf veins, covering entire leaf', 'Leaves', 'Overwinters in infected corn debris. Conidia spread by wind. Minimum tillage increases disease risk.', '14-21 days', 'Copper-based sprays preventively', 'Azoxystrobin, Propiconazole, Pyraclostrobin at tasseling stage', 'Bacillus subtilis', 'Hybrid resistance, crop rotation, tillage to bury debris, fungicide at VT/R1', 'Preventive spray at VT stage', '14-21 days', 21, '2026-06-26 15:47:47'),
    (22, 'Late Blight (Potato)', 'Phytophthora infestans', 'Oomycete', 'Potato', 'Potato, Tomato', 'Critical', 'World''s most economically important plant disease. Caused Irish Potato Famine. Global annual losses > $10 billion.', 'Worldwide', 'Cool (10-20°C), wet weather, humidity >90%, dew', 'Water-soaked pale green spots on leaves, white sporulation on underside in humid conditions', 'Dark brown-black lesions on leaves, brown rots on stems, rapid spread of entire field collapse, tuber rot (brown-red internal)', 'Leaves, Stems, Tubers', 'Survives as oospores in soil and in infected tubers. Spreads by zoospores and sporangia. Wind dispersal over long distances.', '2-4 days under optimal conditions', 'Copper hydroxide (2.5-3g/L) preventively, Bordeaux mixture, avoid excessive irrigation', 'Metalaxyl-M + Mancozeb 2.5g/L, Dimethomorph + Mancozeb, Cymoxanil + Famoxadone, Fluopicolide', 'Bacillus subtilis QST713, Bacillus amyloliquefaciens', 'Plant resistant varieties (Kufri Bahar, Jyoti), use certified disease-free seed tubers, apply fungicide before first rains, destroy volunteer plants', 'Every 5-7 days during high-risk weather (Blitecast model advisory)', 'Preventive only; infected plants rarely recover', 7, '2026-06-26 15:47:47'),
    (23, 'Common Scab', 'Streptomyces scabies', 'Bacterial (Actinomycete)', 'Potato', 'Potato, Beet, Radish, Carrot', 'Medium', 'Reduces tuber quality and marketability by 10-40%.', 'Worldwide, especially alkaline sandy soils', 'Alkaline soils (pH > 5.5), dry soil during tuber initiation, temperatures 20-22°C', 'No visible early symptoms on foliage', 'Brown corky scab lesions (raised, sunken, or russeted) on tuber surface; external quality defect only', 'Tubers (surface)', 'Soil-borne bacteria, survive indefinitely. Infection during early tuber formation through lenticels and wounds.', '14-30 days from tuber initiation', 'Soil acidification (sulfur), crop rotation, adequate irrigation during tuber formation', 'Quintozene PCNB seed treatment (limited), Flutolanil seed treatment', 'Fluorescent Pseudomonas, Bacillus subtilis soil inoculants', 'Lower soil pH to 5.0-5.5, maintain soil moisture during tuber initiation, rotate with non-susceptible crops (cereals), use scab-resistant varieties', 'Management practices; no effective spray treatment', 'Prevention focus', NULL, '2026-06-26 15:47:47'),
    (24, 'Anthracnose', 'Colletotrichum gloeosporioides', 'Fungal', 'Mango', 'Mango, Papaya, Avocado, many tropical fruits', 'High', 'Most important post-harvest mango disease; causes 30-80% market loss.', 'All tropical and subtropical mango-growing regions', 'High humidity, rainfall, temperatures 25-30°C, especially during flowering and fruit development', 'Dark brown to black spots on young leaves, flowers, and immature fruits; ''blossom blight'' killing flower clusters', 'Sunken, dark brown lesions on mature fruits that expand rapidly post-harvest; fruit rot; complete flower destruction', 'Leaves, Flowers, Young Shoots, Fruit', 'Survives in infected twigs and mummified fruits. Conidia spread by rain and dew. Quiescent infection in unripe fruit activated during ripening.', '7-14 days', 'Copper oxychloride 3g/L, neem oil + copper, hot water dip 52°C for 5 minutes (post-harvest)', 'Carbendazim 0.1% + Mancozeb 0.25% spray, Azoxystrobin + Difenoconazole, Propiconazole 0.1%', 'Trichoderma, Bacillus subtilis, Pseudomonas fluorescens', 'Prune dead wood, copper spray before flowering, proper post-harvest handling (hot water), waxing, cold chain', '3-4 sprays during flowering and fruit development; every 10-14 days', 'Prevention focus; treat within 1-2 days post-harvest', 7, '2026-06-26 15:47:47'),
    (25, 'Powdery Mildew (Mango)', 'Oidium mangiferae', 'Fungal', 'Mango', 'Mango', 'High', 'Destroys 10-80% of flowers; critical during mango flowering season.', 'All mango-growing regions', 'Dry weather with low humidity at night, temperatures 10-20°C at night, 25-35°C during day (classic powdery mildew conditions)', 'White powdery coating on young leaves, flower clusters, and young fruits', 'Complete whitening of panicles, flower drop, young fruit drop, malformed surviving fruits', 'Young Leaves, Flowers (panicles), Young Fruits', 'Spreads by airborne conidia. Favored by dry nights and warm days during flowering season.', '7-10 days', 'Wettable sulfur 3g/L at bud break; diluted milk spray (1:5); potassium bicarbonate', 'Triadimefon 25% WP (1g/L), Hexaconazole 5% EC (2ml/L), Propiconazole 25% EC (1ml/L), Myclobutanil', 'Bacillus subtilis, Ampelomyces quisqualis', 'First spray at bud emergence, second at fruit set; avoid overhead irrigation; morning sprays', '3 sprays at 15-day intervals during flowering season', '7-10 days with treatment', 21, '2026-06-26 15:47:47'),
    (26, 'Mango Malformation Disease (MMD)', 'Fusarium mangiferae', 'Fungal', 'Mango', 'Mango', 'High', 'Infected trees produce no marketable fruits; economically devastating especially in India and Egypt.', 'India, Pakistan, Egypt, South Africa, USA, Brazil', 'Cool weather, high humidity, specific Fusarium strains', 'Vegetative malformation: bunchy top appearance with compacted proliferation of shoots (''mango witches'' broom'')', 'Floral malformation: panicle conversion to compact, sterile, green vegetative structure; no fruits formed', 'Shoot tips, Flower panicles', 'Systemically infects vascular tissue. Spread by infected scion material, mite vectors (Aceria mangiferae), and contaminated tools.', 'Months to years (systemic)', 'Remove and burn malformed parts; control mites with acaricides', 'NAA (Naphthaleneacetic acid) 200ppm spray + Carbendazim (0.1%) at panicle emergence', 'No effective biological control', 'Use disease-free planting material, certified nursery plants, deinfest cutting tools, control mite vectors', 'Pruning and NAA spray at panicle initiation', 'Partial control; severely affected trees may need replacement', 30, '2026-06-26 15:47:47'),
    (27, 'Panama Wilt (Fusarium Wilt of Banana)', 'Fusarium oxysporum f. sp. cubense (TR4)', 'Fungal', 'Banana', 'Banana, Plantain', 'Critical', 'TR4 strain virtually eliminated Gros Michel variety globally. Threatens Cavendish. No effective cure.', 'Worldwide', 'Warm soils, pH 4.5-6.0, poor drainage, 24-34°C', 'Yellowing of older outer leaves, leaf collapse, starting from leaf margins; brown streaking in pseudostem when cut', 'Complete plant collapse, pseudostem brown-red internal discoloration from base upward, no fruit production', 'Roots, Pseudostem (vascular), Leaves', 'Soil-borne chlamydospores survive for decades. Enter through roots. Clog xylem vessels. Spreads through soil water and contaminated tools.', 'Weeks to months depending on race and soil', 'No cure. Soil solarization, biological soil amendments (Trichoderma, compost)', 'No effective chemical treatment', 'Trichoderma koningii, T. harzianum as suppressants', 'Strict quarantine, plant resistant varieties (GCTCV-218 for TR4), clean tools with bleach, avoid infected soil movement', 'Preventive soil treatment only', 'No recovery; replant with resistant varieties', NULL, '2026-06-26 15:47:47'),
    (28, 'Black Sigatoka (Black Leaf Streak)', 'Pseudocercospora fijiensis', 'Fungal', 'Banana', 'Banana, Plantain', 'High', 'Without fungicide, can reduce banana yield by 35-50%. Increases fungicide cost by $1000/ha/year.', 'Most banana-growing areas worldwide', 'High humidity, rainfall, temperatures 27-30°C', 'Tiny pale yellow flecks on lower leaf surface that elongate into brown streaks', 'Brown-black elongated lesions with yellow halo on upper leaf surface; premature defoliation; green fruit ripening prematurely', 'Leaves', 'Spores (conidia and ascospores) spread by wind and rain. Multiple infection cycles per season. Develops resistance to fungicides rapidly.', '25-50 days', 'Copper oxychloride (2-3g/L) sprays, oil-based copper formulations; remove infected leaves', 'Systemic fungicides on rotation: Propiconazole, Tebuconazole, Fenbuconazole, Chlorothalonil; resistance management essential', 'No effective biocontrol registered', 'Resistant varieties, remove lower infected leaves (deleafing), reduce humidity with good drainage and canopy management', '12-24 sprays per year depending on disease pressure', 'Ongoing management; no cure', 7, '2026-06-26 15:47:47'),
    (29, 'Cotton Leaf Curl Virus Disease (CLCuD)', 'Cotton leaf curl Multan virus (CLCuMV) + betasatellite', 'Viral', 'Cotton', 'Cotton, Okra, Hibiscus, Tomato', 'Critical', 'Devastated Pakistan cotton industry in 1992-93 causing 30% production loss. Ongoing threat to South Asia.', 'Pakistan, India, Nigeria, Sudan', 'High whitefly populations, temperatures 25-35°C', 'Upward curling of leaves, vein thickening, enations (leaf-like outgrowths) on underside of leaves', 'Severe stunting, dark green thickened curled leaves, no boll formation, plant death', 'Leaves, Entire plant', 'Transmitted by whitefly (Bemisia tabaci) in persistent circulative manner. No mechanical or seed transmission.', '14-21 days', 'Control whiteflies with neem extract, reflective mulch, remove infected plants', 'Imidacloprid/Thiamethoxam soil application for whitefly control; Acetamiprid foliar spray', 'Encarsia formosa, Beauveria bassiana for whitefly control', 'Resistant varieties (NIAB 846, CIM-499), control whiteflies strictly, remove infected plants, use insect-proof nets in nursery', 'Whitefly control every 7-10 days', 'No recovery; remove infected plants', NULL, '2026-06-26 15:47:47'),
    (30, 'Damping Off', 'Pythium spp., Rhizoctonia solani, Fusarium spp.', 'Fungal / Oomycete', 'All vegetable and field crops in seedling stage', 'All vegetable and field crops in seedling stage', 'High', 'Can destroy 50-100% of seedlings in affected nursery beds.', 'Worldwide', 'Excess soil moisture, poor drainage, dense seeding, high humidity, cool conditions', 'Seeds fail to germinate (pre-emergence damping off), or seedlings collapse just below soil level (post-emergence)', 'Water-soaked ''pinched'' stem at soil level, seedling falls over, dark discoloration at base', 'Stem base, Hypocotyl, Roots', 'Soil-borne pathogens; sporangia and oospores persist in soil. Activated by excess moisture.', '1-3 days', 'Chilled neem cake in soil, well-drained media, Trichoderma seed treatment, chamomile tea drench', 'Metalaxyl 35% DS seed treatment, Captan 50% WP seed treatment (2g/kg), copper sulfate soil drench', 'Trichoderma harzianum seed treatment, Pseudomonas fluorescens soil drench', 'Use sterile nursery media, avoid overwatering, thin seedlings, use well-drained trays, treat seeds before sowing', 'Soil treatment before sowing; drench after symptom appearance', 'Remove affected seedlings; re-sow treated seeds', NULL, '2026-06-26 15:47:47'),
    (31, 'Crown Gall', 'Agrobacterium tumefaciens (Rhizobium radiobacter)', 'Bacterial', 'Rose, Fruit trees (apple, cherry, walnut), Grapes, more than 600 species', 'Rose, Fruit trees (apple, cherry, walnut), Grapes, more than 600 species', 'Medium', 'Reduces tree lifespan, productivity by 20-50% in affected orchards.', 'Worldwide', 'Wounds (from pruning, transplanting, frost damage), alkaline soils', 'Small, soft, round galls develop at crown (soil line) or on roots', 'Galls enlarge to large rough, brown, corky tumors; reduced plant vigor, stunting, increased susceptibility to other diseases', 'Crown, Roots, Stems', 'Soil-borne; bacterium transfers its own DNA (T-DNA) into plant cells causing tumor growth. Spreads through soil water and infected tools.', 'Weeks to months', 'Cut out galls; treat with Agrobacterium radiobacter strain K-84 (biocontrol) at planting', 'No effective post-infection treatment; copper bactericides preventively', 'Agrobacterium radiobacter strain K-84 / K-1026 biocontrol (prevents infection)', 'Avoid wounding, use K-84 dip on roots before planting, plant only certified gall-free material', 'Root dip at planting', 'No cure; prune and disinfect tools with bleach', NULL, '2026-06-26 15:47:47'),
    (32, 'Botrytis Gray Mold', 'Botrytis cinerea', 'Fungal', '> 1000 plant species including grapes, strawberry, rose, tomato, lettuce, onion', '> 1000 plant species including grapes, strawberry, rose, tomato, lettuce, onion', 'High', 'Second most important fungal plant pathogen worldwide (after Magnaporthe). Major greenhouse and soft fruit pathogen.', 'Worldwide', 'Cool temperatures (15-20°C), high humidity >95%, damaged or senescent tissue', 'Water-soaked, brown lesions on petals, leaves, and stems; soft rot', 'Characteristic gray fluffy fungal sporulation covering lesions; blight of flowers, stem cankers, fruit rot ("ghost spot" on tomato)', 'Flowers, Leaves, Stems, Fruit, Storage organs', 'Ubiquitous saprophyte; infects through wounds, senescent tissue. Gray conidial masses spread by air and handling. Sclerotia overwinter in soil.', '2-4 days', 'Remove infected tissue, improve air circulation, reduce humidity; Bacillus subtilis, Trichoderma spray', 'Iprodione (1.5g/L), Pyrimethanil (1ml/L), Fenhexamid (1g/L), Cyprodinil (0.5g/L). Rotate fungicides for resistance management.', 'Bacillus subtilis QST713 (Serenade), Trichoderma asperellum, Clonostachys rosea (Prestop)', 'Improve air circulation, avoid wounding, remove dead tissue, avoid waterlogging, maintain low humidity', 'Every 7-10 days under disease pressure; preventive at flowering', '7-14 days with treatment', 1, '2026-06-26 15:47:47'),
    (33, 'Sclerotinia Stem Rot (White Mold)', 'Sclerotinia sclerotiorum', 'Fungal', '> 400 species: Canola, Soybean, Sunflower, Bean, Carrot, Celery', '> 400 species: Canola, Soybean, Sunflower, Bean, Carrot, Celery', 'High', 'Major pathogen of oilseeds and legumes worldwide; 10-60% yield loss.', 'Worldwide temperate regions', 'Cool temperatures (15-20°C), high humidity, wet soil, dense canopy', 'Water-soaked lesions on lower stems and branches; bleached, straw-colored stem tissue', 'White cottony mycelial growth inside and outside infected tissue, large hard black sclerotia (2-10mm) inside stem', 'Stem (basal), Branches, Pods/Siliques', 'Sclerotia survive in soil 3-5+ years. Apothecia (mushroom-like structures) release ascospores during flowering. Infection through flowers.', '7-14 days', 'Thiram-treated seeds, adequate plant spacing, crop rotation', 'Thiophanate-methyl (1g/L), Boscalid (0.5g/L), Iprodione, Fluazinam at early flowering', 'Coniothyrium minitans (Contans WG) — applied to soil to parasitize sclerotia', 'Crop rotation (non-host crops for 3+ years), avoid dense planting, improve drainage', 'At early bloom; repeat once in 10-14 days', '14-21 days', 14, '2026-06-26 15:47:47');

DROP TABLE IF EXISTS plant_pests CASCADE;
CREATE TABLE plant_pests (
    id INTEGER PRIMARY KEY NOT NULL,
    pest_name VARCHAR(200) NOT NULL,
    scientific_name VARCHAR(300) NULL,
    order_name VARCHAR(100) NULL,
    family_name VARCHAR(100) NULL,
    pest_category VARCHAR(100) NULL,
    host_plants VARCHAR(255) NULL,
    geographic_distribution VARCHAR(255) NULL,
    damage_type VARCHAR(200) NULL,
    identification_tips VARCHAR(255) NULL,
    damage_symptoms VARCHAR(255) NULL,
    lifecycle_summary VARCHAR(255) NULL,
    seasonal_peak VARCHAR(200) NULL,
    economic_threshold VARCHAR(200) NULL,
    organic_control VARCHAR(255) NULL,
    chemical_control VARCHAR(255) NULL,
    biological_control VARCHAR(255) NULL,
    ipm_notes VARCHAR(255) NULL,
    natural_predators VARCHAR(255) NULL,
    resistance_issues VARCHAR(255) NULL,
    created_at TIMESTAMP NULL
);

-- Data for plant_pests (17 rows)
INSERT INTO plant_pests (id, pest_name, scientific_name, order_name, family_name, pest_category, host_plants, geographic_distribution, damage_type, identification_tips, damage_symptoms, lifecycle_summary, seasonal_peak, economic_threshold, organic_control, chemical_control, biological_control, ipm_notes, natural_predators, resistance_issues, created_at) VALUES
    (1, 'Whitefly', 'Bemisia tabaci', 'Hemiptera', 'Aleyrodidae', 'Sucking_Pests', 'Tomato, Cotton, Pepper, Cucumber, Cassava, Sweet Potato, Bean', 'Tropical and subtropical worldwide', 'Sucking', 'Tiny (1-1.5mm) white-winged insects; fly in clouds when disturbed; yellowish oval nymphs on leaf underside', 'Yellowing leaves, sticky honeydew, sooty mold (secondary), vector of 200+ plant viruses (TYLCV, CLCuD, CBSD, cassava mosaic)', '{"egg": "Scale-like, yellow, on leaf underside; hatches in 5-7 days", "nymph": "4 instars; flat, oval, scale-like; 10-15 days", "pupa": "Waxy pupal case; 4-6 days", "adult": "Tiny white moth-like; lives 30-40 days; female lays 150-200 eggs", "total_duration_days": "24-28 days; multiple overlapping generations"}', 'Summer/dry season when populations explode', '5-10 adults per leaf, 1 adult per yellow sticky trap per day', 'Yellow sticky traps, neem oil + soap spray (5ml+2ml per L), reflective mulch, soap water spray, Beauveria bassiana', 'Imidacloprid 17.8% SL (0.5ml/L), Thiamethoxam 25% WG (0.2g/L), Acetamiprid 20% SP (0.2g/L), Spiromesifen (resistance management)', 'Encarsia formosa (parasitic wasp), Eretmocerus mundus, Macrolophus pygmaeus (predatory bug), Beauveria bassiana', 'Rotate between chemical classes to manage resistance; use systemic at transplanting, contact at adult stage; banker plant system in greenhouses', 'Encarsia formosa, Eretmocerus mundus, Chrysoperla carnea, Macrolophus pygmaeus', 'B. tabaci MEAM1 and MED biotypes highly resistant to neonicotinoids and pyrethroids', '2026-06-26 15:47:47'),
    (2, 'Aphids', 'Myzus persicae (Green Peach Aphid); multiple species', 'Hemiptera', 'Aphididae', 'Sucking_Pests', 'Universal — thousands of plant species (vegetables, fruits, ornamentals, cereals)', 'Worldwide', 'Sucking; Virus vector', 'Soft-bodied 1-3mm insects, green/yellow/black/pink depending on species; winged and wingless forms; two cornicles (tail tubes) on abdomen', 'Leaf curling, distortion, yellowing; sticky honeydew with black sooty mold; severe infestations stunt plants; vectors of 200+ plant viruses (CMV, PVY, BYDV)', '{"parthenogenetic": "Females reproduce without mating in spring/summer; 7-10 days per generation", "sexual": "Sexual cycle in autumn; overwinter as eggs on woody hosts", "total_duration_days": "7-10 days per generation; up to 50 generations per year"}', 'Spring and early summer; warm dry conditions', '10-25 aphids per leaf; or any number when virus risk is high', 'Strong water spray to dislodge; insecticidal soap (1%); neem oil (3-5ml/L); garlic-pepper spray; encourage natural enemies', 'Imidacloprid 17.8% SL (0.3ml/L), Dimethoate 30% EC (2ml/L), Flonicamid, Pymetrozine, Spirotetramat', 'Coccinella septempunctata (ladybug), Chrysoperla carnea (lacewing), Aphidius colemani and A. ervi (parasitic wasps), Syrphid fly larvae', 'Banker plant systems (cereal aphid + parasitoid) used in greenhouses; avoid broad-spectrum insecticides that kill natural enemies', 'Ladybugs (Coccinella sp.), Lacewings (Chrysoperla sp.), Syrphid flies, Parasitic wasps (Aphidius sp.), Ground beetles', 'M. persicae has developed resistance to organophosphates, carbamates, and some neonicotinoids', '2026-06-26 15:47:47'),
    (3, 'Thrips', 'Thrips palmi (Melon Thrips); Frankliniella occidentalis (Western Flower Thrips)', 'Thysanoptera', 'Thripidae', 'Sucking_Pests', 'Virtually all vegetables, ornamentals, fruits, cotton, onion, cereal crops', 'F. occidentalis: worldwide; T. palmi: tropical Asia/Pacific', 'Rasping/sucking; Virus vector (TSWV, CSNV)', 'Very small (0.5-1.5mm); slender, fringed wings; yellow to dark brown depending on species; move fast', 'Silvery streaks/scarring on leaves and fruits (from feeding); distorted growth; ''ghost spots'' on petals; TSWV virus symptoms (wilting, bronzing, ring spots)', '{"egg": "Inserted in plant tissue; hatches 3-5 days", "nymph": "2 nymphal stages; 7-10 days", "prepupa_pupa": "In soil or leaf debris; 3-7 days", "adult": "Lives 30-45 days; female lays 150-300 eggs", "total_duration_days": "14-22 days at optimal temperature (25-30\u00b0C)"}', 'Hot dry conditions; population explosions common', '5-10 thrips per flower; 1 per sticky trap per day for virus-risk crops', 'Blue sticky traps (most attractive to thrips), spinosad spray, neem oil, kaolin clay, predatory mites (Neoseiulus cucumeris)', 'Spinosad 45% SC (0.3ml/L), Imidacloprid, Abamectin 1.9% EC (0.5ml/L), Cyantraniliprole, Tolfenpyrad', 'Neoseiulus cucumeris, Amblyseius swirskii (predatory mites); Orius insidiosus (pirate bug); Steinernema feltiae (entomopathogenic nematode) for soil pupae', 'Hard to control due to hidden feeding in flowers and leaf tissue; soil pupae require soil drenches; rotate chemical classes', 'Orius spp. (pirate bugs), Predatory mites (Neoseiulus, Amblyseius), Ground beetles, Lacewings', 'F. occidentalis has developed resistance to many insecticide classes', '2026-06-26 15:47:47'),
    (4, 'Spider Mite (Two-Spotted)', 'Tetranychus urticae', 'Trombidiformes', 'Tetranychidae', 'Sucking_Pests', 'Over 1,100 plant species: all vegetables, ornamentals, fruits, cotton, soybean', 'Worldwide, especially hot dry conditions', 'Cell content feeding', 'Tiny (< 0.5mm); two dark spots on pale greenish-yellow body; spin fine silk webbing on leaf underside; visible under hand lens', 'Stippled (tiny pale dots/punctures) on leaves from below; leaves turn bronze/yellow and dry; fine silk webbing; premature defoliation', '{"egg": "Spherical, transparent; hatches 3-5 days", "larva_nymph": "Larva + 2 nymphal stages; 7-10 days", "adult": "Female lives 30 days; lays 10-20 eggs/day", "total_duration_days": "10-14 days at 30\u00b0C; up to 20 generations/year"}', 'Hot dry summer; mites thrive in low humidity and warm conditions', '20-50 mites per leaf; or visible stippling on > 30% of scouted leaves', 'Water spray to wash off; neem oil 5ml/L; wettable sulfur 3g/L; insecticidal soap; predatory mites release; soap solution sprays', 'Abamectin 1.9% EC (0.5ml/L), Spiromesifen 22.9% SC (1ml/L), Hexythiazox 5% EC (1ml/L), Bifenazate, Clofentezine, Fenpyroximate', 'Phytoseiulus persimilis (excellent predator), Amblyseius californicus, Neoseiulus californicus, Feltiella acarisuga (gall midge)', 'Rotate acaricides by chemical class; preserve natural enemies; increase irrigation in dry weather to reduce mite-favorable conditions; do NOT use broad-spectrum insecticides that kill predatory mites', 'Phytoseiulus persimilis, Galendromus occidentalis, Stethorus punctillum (ladybug), Feltiella acarisuga, Chrysoperla', 'Extremely prone to developing acaricide resistance; use rotation strictly', '2026-06-26 15:47:47'),
    (5, 'Mealybugs', 'Phenacoccus solenopsis (Cotton Mealybug); Planococcus citri (Citrus Mealybug)', 'Hemiptera', 'Pseudococcidae', 'Sucking_Pests', 'Cotton, Grapes, Citrus, Mango, Cassava, ornamentals, vegetables', 'Tropical and subtropical worldwide', 'Sucking; Honeydew production; Virus vector', 'Soft, oval, covered with white mealy wax; pink body visible through wax; waxy filaments around body; colonies in leaf axils and stem crevices', 'Yellowing, leaf drop, honeydew + sooty mold; cotton twisting; mango malformation spread; overall plant decline and death in severe infestations', '{"egg": "Females lay 200-600 eggs in egg sac under body", "crawler": "First instar (crawler) most vulnerable stage; spreads by wind, ants, contaminated tools", "total_duration_days": "30-60 days per generation; 5-6 generations/year in warm conditions"}', 'Peak in spring and autumn; protected by ants', '1-2 mealybugs per plant in nursery; 5% infested plants in field', 'Neem oil + soap spray; rubbing alcohol on cotton swabs; strong water spray; remove waxy coating first; Cryptolaemus montrouzieri release', 'Imidacloprid soil drench (2ml/L), Buprofezin 25% WP (1g/L), Chlorpyrifos 20% EC (2.5ml/L), Acetamiprid + Chlorpyrifos', 'Cryptolaemus montrouzieri (mealybug destroyer beetle), Leptomastix dactylopii (parasitoid wasp), Anagyrus kamali, Acerophagus papayae', 'Control ants (which protect mealybugs from predators); reach under waxy coating with oil-based sprays; ant management improves biocontrol effectiveness', 'Cryptolaemus montrouzieri, Leptomastix dactylopii, Anagyrus kamali, Lacewings', 'Moderate; rotate chemical classes', '2026-06-26 15:47:47'),
    (6, 'Scale Insects', 'Diaspidiotus perniciosus (San Jose Scale); Saissetia oleae (Olive Scale)', 'Hemiptera', 'Diaspididae / Coccidae', 'Sucking_Pests', 'Fruit trees (apple, pear, citrus, mango), olives, ornamentals', 'Worldwide', 'Sucking', 'Round to oyster-shaped waxy armor covering body; armored scales (Diaspididae) - armor separable from body; soft scales (Coccidae) - armor inseparable', 'Yellowing, twig and branch death, reduced fruit quality, bark encrustation; honeydew (soft scales) leading to sooty mold', '{"crawler": "Mobile first instar spreads by wind and contact; settles and secretes scale", "total_duration_days": "1-2 generations per year for most scale species"}', 'Crawler emergence in spring', 'Variable; 5 per 10cm branch for San Jose scale', 'Dormant oil spray (petroleum oil 3-5%) at crawler stage; white summer oil (1-2%); brush off with stiff brush', 'Buprofezin (at crawler stage), Chlorpyrifos + oil, Spirotetramat systemic; dormant oil during winter', 'Encarsia perniciosi (parasitoid of San Jose scale), Comperiella bifasciata, Aphytis melinus (red scale parasitoid)', 'Timing at crawler stage is critical; inspect bark regularly; monitor with sticky tape to detect crawlers', 'Aphytis sp. wasps, Encarsia sp. wasps, Chilocorus ladybugs, Cryptolaemus', 'Low to moderate', '2026-06-26 15:47:47'),
    (7, 'Leafhoppers', 'Amrasca biguttula biguttula (Cotton/Okra Leafhopper); Empoasca spp.', 'Hemiptera', 'Cicadellidae', 'Sucking_Pests', 'Cotton, Okra, Brinjal, Potato, Grape, Legumes', 'Worldwide', 'Sucking; Virus vector; Toxicogenic saliva', 'Wedge-shaped, 3-4mm; green/yellow; jump sideways when disturbed; run diagonally on plants', 'Cotton: ''Cotton leaf curl'' or ''Jassid damage'' — leaf edge curling upward, reddening; Potato/Brinjal: leaf hopper burn (hopperburn) — marginal leaf scorch and curling', '{"egg": "Inserted in leaf midrib; hatches 6-10 days", "nymph": "5 instars; wingless; 15-20 days", "adult": "3-4 weeks; lays 50-100 eggs", "total_duration_days": "25-30 days; 5-6 generations/year"}', 'Hot, dry conditions', '2 nymphs per leaf for cotton; 5 per leaf for brinjal', 'Neem seed kernel extract 5%, neem oil; yellow sticky traps; Beauveria bassiana spray', 'Imidacloprid 17.8% SL (0.3ml/L), Lambda-cyhalothrin 5% EC (1ml/L), Thiamethoxam, Dimethoate 30% EC (2ml/L)', 'Anagrus atomus (egg parasitoid in grapes), Gonatocerus ashmeadi, Stethorus ladybugs', 'Spray lower leaf surface; morning sprays most effective; hairy-leaved cultivars are less susceptible', 'Anagrus atomus (parasitoid wasp), General predators (ladybugs, lacewings)', 'Moderate resistance to organophosphates documented', '2026-06-26 15:47:47'),
    (8, 'Diamondback Moth', 'Plutella xylostella', 'Lepidoptera', 'Plutellidae', 'Chewing_Caterpillars', 'Cabbage, Cauliflower, Broccoli, Kale, Mustard, Turnip — all Brassica crops', 'Worldwide; most severe in tropics and subtropics', 'Leaf feeding', 'Adult: 8mm, gray-brown moth with diamond pattern on back when wings folded; Larva: pale green, 10mm, wriggle violently when disturbed, dangle from silk thread', 'Windowing: larvae eat leaf tissue from below, leaving translucent papery epidermis on upper surface; total leaf skeletonization in heavy infestations; head borer', '{"egg": "Oval, flattened, on leaf surface; hatches 3-8 days", "larva": "4 instars; 8-14 days", "pupa": "White cocoon on leaf; 5-10 days", "adult": "Lives 4-8 days; lays 150-300 eggs", "total_duration_days": "18-30 days; 10-15 generations/year in tropics"}', 'Year-round in tropics; peaks in dry season when conditions are hot', '1 larva per plant at transplanting; 5 larvae per plant after establishment', 'Bacillus thuringiensis subsp. kurstaki (Bt-k) spray (most effective); neem seed kernel extract 5%; hand picking; pheromone traps for monitoring', 'Spinosad 45% SC (0.3ml/L), Indoxacarb 14.5% SC (1ml/L), Chlorfluazuron (IGR), Emamectin benzoate 5% SG (0.2g/L), Flubendiamide', 'Cotesia plutellae (parasitic wasp), Diadegma semiclausum, Diadromus collaris; Bacillus thuringiensis', 'World''s most insecticide-resistant insect pest. Resistance management is critical. Rotate between Bt, spinosad, indoxacarb, and diamide insecticides.', 'Cotesia plutellae, Diadegma semiclausum, Chrysoperla, Spiders', 'Extreme resistance to virtually all insecticide classes; critical resistance management needed', '2026-06-26 15:47:47'),
    (9, 'Fall Armyworm', 'Spodoptera frugiperda', 'Lepidoptera', 'Noctuidae', 'Chewing_Caterpillars', 'Maize (primary), Sorghum, Rice, Sugarcane, Cotton, Tomato, 350+ plant species', 'Native to Americas; invaded Africa (2016), Asia (2018), Australia (2020); now worldwide', 'Leaf and whorl feeding; ear damage', 'Adult: 38mm wingspan, mottled gray-brown moths; Larva: greenish to brown, inverted ''Y'' mark on head, 4 square black dots on 8th abdominal segment, up to 40mm', 'Ragged windows in leaves; characteristic ''shot hole'' damage in whorl; frass in leaf whorl; direct ear damage (in maize); can completely defoliate young plants', '{"egg": "Mass of 100-200 eggs covered with scales on leaf surface; hatches 3-5 days", "larva": "6 instars; 14-30 days", "pupa": "In soil; 8-14 days", "adult": "10-20 day lifespan; female lays 1500+ eggs", "total_duration_days": "30-50 days; 3-6 generations/year"}', 'Peak during main maize season; migrates with wind systems', '2 egg masses or 5 larvae per 100 plants (maize); or any visible whorl damage > 5%', 'Bt-kurstaki or Bt-aizawai spray; fall armyworm pheromone traps; sand+soil in whorl (suffocates larvae); egg mass and larvae hand collection', 'Emamectin benzoate 5% SG (0.4g/L into whorl), Chlorantraniliprole (Coragen), Spinetoram, Lambda-cyhalothrin (adult moths)', 'Telenomus remus (egg parasitoid), Cotesia icipe, Coccygomimus turionellae, Metarhizium rileyi, NPV (Nuclear Polyhedrosis Virus)', 'Scouting critical: check whorls for frass and larvae early. Early stage intervention most effective. Avoid broad-spectrum insecticides to preserve natural enemies.', 'Telenomus remus (egg parasitoid), Cotesia sp., Ear wigs, Ground beetles, Ants (eat eggs)', 'Developing resistance to Bt proteins in some regions; resistance to pyrethroid-based insecticides emerging', '2026-06-26 15:47:47'),
    (10, 'Cotton Bollworm (Helicoverpa)', 'Helicoverpa armigera', 'Lepidoptera', 'Noctuidae', 'Chewing_Caterpillars', 'Cotton, Chickpea, Tomato, Maize, Pigeonpea, Sorghum — polyphagous pest of 200+ species', 'Old World (Afro-Eurasia); H. zea in Americas', 'Fruit, flower and seed feeding', 'Adult: 35-40mm wingspan, yellowish-brown with dark spot; Larva: variable color (green/brown/pinkish), microspines on body, up to 40mm', 'Entry holes in cotton bolls (with frass-filled tunnels), tomato fruit damage, chickpea pod damage with grain loss, maize kernel damage', '{"egg": "Round, ribbed; on upper leaf surface or flowers; hatches 2-4 days", "larva": "6 instars; 14-28 days", "pupa": "In soil; 14-28 days", "adult": "5-15 days; female lays 500-1500 eggs", "total_duration_days": "30-70 days; 2-5 generations/year"}', 'Kharif (monsoon) season in South Asia; depends on crop', '1-2 larvae per plant (cotton); 5% fruit infestation', 'NPV spray (2×10¹² POB/ha); HaNPV + cotton Bt; pheromone traps (1/ha); neem seed kernel extract; Bt-k spray', 'Emamectin benzoate 5% SG (0.4g/L), Chlorantraniliprole 18.5% SC (0.3ml/L), Indoxacarb, Flubendiamide, Thiodicarb', 'Trichogramma chilonis (egg parasitoid, 1 lakh/ha weekly), Habrobracon hebetor, Chrysoperla carnea, HaNPV', 'Bt crops (Bt cotton, Bt chickpea) used widely; pyrethroid resistance widespread; refuge strategy essential with Bt crops; pheromone trap-based monitoring', 'Trichogramma sp. (egg parasitoids), Habrobracon hebetor (larva parasitoid), Campoletis chlorideae, Chrysoperla carnea', 'High resistance to pyrethroids and organophosphates; Cry1Ac resistance documented in Australia; critical resistance monitoring needed', '2026-06-26 15:47:47'),
    (11, 'Yellow Stem Borer (Rice)', 'Scirpophaga incertulas', 'Lepidoptera', 'Crambidae', 'Chewing_Caterpillars', 'Rice (primary), Sugarcane, Wild grasses', 'South and Southeast Asia', 'Stem boring', 'Adult: white moth, 25-30mm wingspan; female has black spot; Larva: creamy white, dark head, up to 20mm', 'Deadheart: young plants central leaf whorl dies and turns brown (easy to pull out) — vegetative stage; Whitehead: panicle turns white and empty — reproductive stage', '{"egg": "Flat oval masses (50-100 eggs) on leaf blades; hatches 5-7 days", "larva": "Bore into stems; 5 instars; 30-35 days", "pupa": "Inside stem; 7-10 days", "adult": "5-7 days; female lays 100-300 eggs", "total_duration_days": "45-55 days; 2-4 generations/season"}', 'High during Kharif paddy; light traps show seasonal peaks', '5% deadheart at vegetative stage; 2% whitehead at flowering stage', 'Clip leaf tips of transplanted seedlings (removes egg masses); light traps; pheromone traps; release Trichogramma japonicum', 'Cartap hydrochloride 4G granules (25 kg/ha in standing water), Chlorpyrifos 20% EC (2ml/L), Carbofuran 3G, Fipronil 0.3G', 'Trichogramma japonicum (egg parasitoid, 1 lakh/ha at 10-day intervals), Tetrastichus schoenobii, Telenomus rowani', 'Clipping transplant seedlings to remove egg masses is highly effective low-cost management; light traps help reduce adult populations; timing of Trichogramma release is key', 'Trichogramma japonicum, Tetrastichus schoenobii, Spiders, Mirid bugs, Wolf spiders', 'Moderate; less resistance issues than whitefly/DBM', '2026-06-26 15:47:47'),
    (12, 'Fruit Fly (Oriental)', 'Bactrocera dorsalis', 'Diptera', 'Tephritidae', 'Fruit_Pests', 'Mango, Guava, Banana, Papaya, Star Fruit, Citrus — 150+ fruit species', 'Asia, Pacific, Africa (invasive)', 'Oviposition and larval feeding inside fruit', 'Adult: 8mm, yellowish with dark dorsal stripes; distinctive pointed ovipositor in females; red-brown eyes; Larvae: white maggots inside fruit', 'Pin-hole entry with sap/gum oozing; fruit surface discoloration, premature fruit drop; soft rotting interior with white maggots; secondary bacterial and fungal infections', '{"egg": "Inserted into fruit skin in clusters; hatches 1-2 days", "larva": "3 instars inside fruit; 7-14 days", "pupa": "In soil; 8-14 days", "adult": "1-2 months; female lays 1500-2000 eggs", "total_duration_days": "20-30 days; multiple overlapping generations"}', 'Coincides with fruit ripening season; high populations in humid warm conditions', 'Quarantine pest — zero tolerance for export fruit; 1 fly per trap per day for domestic', 'Male attractant traps (Methyl eugenol + malathion or GF-120); fruit bagging with paper or plastic bags; Protein bait sprays; pick and destroy infested fallen fruit', 'Protein bait spray (GF-120 bait + Spinosad); Cover sprays Malathion 50% EC (2ml/L), Dimethoate (2ml/L); only during non-harvest period', 'Fopius arisanus (egg-larval parasitoid), Diachasmimorpha longicaudata, Fopius vandenboschi, mass rearing and release of sterile males (SIT)', 'Bactrocera dorsalis is a major quarantine pest affecting trade. Use of Methyl eugenol + insecticide traps for mass trapping is most effective. Combination: MAT traps + fruit bagging + protein bait + biocontrol', 'Fopius arisanus, Diachasmimorpha longicaudata, Biosteres arisanus', 'Malathion resistance documented; use rotation strategies', '2026-06-26 15:47:47'),
    (13, 'Mango Stone Weevil', 'Sternochetus mangiferae', 'Coleoptera', 'Curculionidae', 'Fruit_Pests', 'Mango (specific to mango seed/stone)', 'Asia, Africa, Americas (invasive)', 'Larval boring into mango seed', 'Adult: 7-9mm, brown-black mottled weevil; Larva: white, legless grub inside mango seed', 'No external fruit damage visible; seed destroyed; premature fruit drop; larvae tunnel through cotyledons; affects seed viability for propagation', '{"egg": "Laid singly in small cavities cut by female in young fruit skin near seed", "larva": "Develop inside seed; 4-6 weeks", "pupa": "Inside seed; 2-3 weeks", "adult": "Emerges when fruit falls; feeds on bark; overwinters in bark crevices", "total_duration_days": "1 generation per year; synchronized with mango fruit season"}', 'Small fruit stage (April-May in India)', 'Quarantine pest for seed trade; 1-2% infestation critical for export', 'Collect and destroy fallen infested fruits; tree hygiene — remove old bark; hot water seed treatment for nursery use (52°C for 15 min)', 'Chlorpyrifos 20% EC (2ml/L) spray when adults are active (Feb-March); trunk banding with insecticide strips', 'No effective commercial biological control', 'Major quarantine pest affecting mango export. Fumigation (Methyl Bromide or Phosphine) required for export. SIT being explored.', 'No significant natural enemies known', 'Low', '2026-06-26 15:47:47'),
    (14, 'White Grubs (Chafer Beetles)', 'Holotrichia consanguinea, Leucopholis lepidophora (multiple spp.)', 'Coleoptera', 'Scarabaeidae', 'Soil_Pests', 'Sugarcane, Groundnut, Maize, Potato, Soybean, Turf grasses, Tree nurseries', 'Worldwide; especially tropical and subtropical regions', 'Root feeding (grubs); adult defoliation', 'Grubs: creamy white C-shaped, up to 30-50mm, brown head; Adults: brown to black beetles 15-35mm with lamellate antennae', 'Plants wilt suddenly (root destruction by grubs); patches of dead plants in field; soil becomes soft and easy to pull plants (roots eaten); adult beetles feed on tree leaves at night', '{"egg": "Laid 10-15cm deep in moist soil; hatches 2-3 weeks", "grub": "3 instars; 9-12 months; main damage period is grub stage", "pupa": "In soil; 3-4 weeks", "adult": "Adult emerges monsoon onset; lives 2-4 weeks; comes to light at night", "total_duration_days": "1 year complete life cycle (some spp. 2-3 years)"}', 'Adults emerge June-July (monsoon); grubs cause damage August-February', '2-3 grubs per square meter', 'Metarhizium anisopliae fungus (1×10⁹ spores/ml) soil application; ploughing to expose and destroy grubs; light traps for adults; neem cake 250 kg/ha', 'Chlorpyrifos 20% EC (5L/ha) soil incorporation before planting; Carbofuran 3G (25 kg/ha); Phorate 10G; Imidacloprid seed treatment', 'Metarhizium anisopliae, Beauveria bassiana soil inoculants; Heterorhabditis bacteriophora (entomopathogenic nematode)', 'Ploughing before monsoon onset exposes grubs to heat and predators; synchronize light trap monitoring with adult emergence; grub management is season-long', 'Birds (mynahs, cattle egret feed on exposed grubs), Ground beetles (Carabidae), Centipedes, Entomopathogenic fungi', 'Developing resistance to chlorpyrifos in some populations', '2026-06-26 15:47:47'),
    (15, 'Root Knot Nematode', 'Meloidogyne incognita, M. javanica, M. arenaria, M. hapla', 'Tylenchida', 'Meloidogynidae', 'Soil_Pests', 'Over 2,000 plant species; especially vegetables, tobacco, cotton, legumes', 'Tropical and subtropical worldwide; most severe in sandy soils', 'Root parasitism; feeding cell formation', 'Microscopic (0.5-1mm); females become sedentary, pear-shaped inside galls; second-stage juveniles (J2) infectious stage; galls visible on roots as swellings', 'Above ground: wilting, chlorosis, stunting resembling nutrient deficiency; Below ground: characteristic root galls (knots), reduced and brown root system, secondary root pathogens', '{"egg": "Eggs in gel matrix (egg mass) on root surface; 200-500 per mass", "j2": "Infectious stage penetrates roots; 5-7 days to hatch", "parasitic_stages": "J3 and J4 inside giant cells; 21-28 days total", "adult_female": "Pear-shaped, sedentary; produces egg mass for next generation", "total_duration_days": "21-30 days per generation at 25\u00b0C; 5-6 generations per season"}', 'All season in warm soils; worse in summer and light sandy soils', '1 egg mass per plant; 10 juveniles per 100ml soil', 'Marigold (Tagetes spp.) intercropping; neem cake 250kg/ha soil application; Paecilomyces lilacinus inoculant; castor cake; mustard cake; crop rotation with cereals', 'Carbofuran 3G (33 kg/ha), Phorate 10G, Ethoprophos 10G at planting; soil fumigation with Dazomet or Metam sodium (pre-plant)', 'Purpureocillium lilacinum (formerly Paecilomyces lilacinus), Pochonia chlamydosporia, Trichoderma harzianum, Bacillus firmus (VOTiVO), Steinernema carpocapsae', 'Soil solarization (polyethylene film on moist soil for 6-8 weeks) highly effective; Mi-1.2 gene resistance in tomato; grafting onto resistant rootstocks effective in cucurbits', 'Predatory nematodes (Steinernema, Heterorhabditis), Predatory fungi (Arthrobotrys), Purpureocillium lilacinum', 'Developing resistance to fumigants and nematicides; Biocontrol is important for sustainable management', '2026-06-26 15:47:47'),
    (16, 'Rice Weevil', 'Sitophilus oryzae', 'Coleoptera', 'Curculionidae', 'Storage_Pests', 'Rice, Wheat, Maize, Barley, Sorghum — stored grains', 'Worldwide; tropical and subtropical regions', 'Grain boring', 'Adult: 2.5-3.5mm, reddish-brown with 4 pale red-yellow spots on elytra; long snout (rostrum); Larvae: white, legless grub inside grain', 'Grain kernels hollowed out; dust and frass in stored grain; characteristic exit holes; grain losses 20-40%; quality deterioration', '{"egg": "Laid inside grain kernel; hatches 3-5 days", "larva": "Develop inside kernel; 4 instars; 15-25 days", "pupa": "Inside grain; 6-10 days", "adult": "4-5 months lifespan; female lays 150-300 eggs", "total_duration_days": "30-40 days per generation; multiple generations in store"}', 'Year-round in warm grain stores; explosive in humid hot conditions', '1 adult per kg grain', 'Clean dry grain storage (< 14% moisture); diatomaceous earth 1.5g/kg mixed with grain; bay leaves in storage; neem leaf powder mixed with grain; hermetic storage (PICS bags, metal silos)', 'Phosphine fumigation (Aluminium phosphide tablets 3 tablets/tonne); Pyrethrin spray on empty stores; Deltamethrin WP on wall surfaces; Pirimiphos-methyl admixture', 'No practical biological control for storage pests', 'Clean storage is the most important preventive measure. Never store wet grain. Use hermetic bags (PICS/GrainPro) for smallholder storage. Monitor with traps regularly.', 'Cheyletus eruditus (predatory mite), Xylocoris flavipes (pirate bug)', 'Phosphine resistance increasingly common; use proper fumigation protocols', '2026-06-26 15:47:47'),
    (17, 'Lesser Grain Borer', 'Rhyzopertha dominica', 'Coleoptera', 'Bostrichidae', 'Storage_Pests', 'Wheat, Rice, Maize, Barley, Sorghum — stored grains', 'Worldwide tropical/subtropical', 'Grain boring from outside', 'Adult: 2.5-3mm, dark brown, elongated with head underneath pronotum; cylindrical shape; Larvae: white grub in grain or debris', 'Flour dust from feeding activity; grain kernels bored from outside; ''rice dust''; severe infestations cause 30-50% losses; heat generation from infested grain', '{"egg": "Laid loose among grain; 3-7 days", "larva": "Feeds externally on grain surface, then penetrates; 4-6 weeks", "pupa": "In grain kernel; 1-2 weeks", "total_duration_days": "5-8 weeks; multiple generations in storage"}', 'Higher temperatures (>25°C) accelerate development', '5 adults per kg grain', 'Hermetic storage, diatomaceous earth, proper drying below 12% moisture', 'Phosphine fumigation, Pirimiphos-methyl grain protectant', 'Limited; Theocolax elegans (ectoparasitoid wasp)', 'More damaging than rice weevil because it attacks hard grain; thrives in lower moisture conditions', 'Theocolax elegans (parasitoid), Xylocoris flavipes', 'Phosphine resistance widespread; resistance monitoring essential', '2026-06-26 15:47:47');

DROP TABLE IF EXISTS botanical_nutrients CASCADE;
CREATE TABLE botanical_nutrients (
    id INTEGER PRIMARY KEY NOT NULL,
    nutrient_name VARCHAR(100) NOT NULL,
    symbol VARCHAR(10) NULL,
    element_type VARCHAR(100) NULL,
    plant_content_range VARCHAR(100) NULL,
    functions VARCHAR(255) NULL,
    deficiency_name VARCHAR(200) NULL,
    deficiency_visual_signs VARCHAR(255) NULL,
    affected_leaves VARCHAR(200) NULL,
    deficiency_crop_specific VARCHAR(255) NULL,
    toxicity_symptoms VARCHAR(255) NULL,
    toxicity_threshold VARCHAR(200) NULL,
    forms_in_soil VARCHAR(255) NULL,
    mobility_in_plant VARCHAR(100) NULL,
    optimal_soil_ph VARCHAR(50) NULL,
    fertilizer_sources VARCHAR(255) NULL,
    critical_crops VARCHAR(255) NULL,
    created_at TIMESTAMP NULL
);

-- Data for botanical_nutrients (18 rows)
INSERT INTO botanical_nutrients (id, nutrient_name, symbol, element_type, plant_content_range, functions, deficiency_name, deficiency_visual_signs, affected_leaves, deficiency_crop_specific, toxicity_symptoms, toxicity_threshold, forms_in_soil, mobility_in_plant, optimal_soil_ph, fertilizer_sources, critical_crops, created_at) VALUES
    (1, 'Carbon', 'C', 'Non-mineral macronutrient', '', '["Primary component of all organic molecules", "Photosynthesis (CO2 fixation)", "Structural component of plant body"]', 'Carbon Deficiency', 'None (CO2 naturally available)', '', '{}', '', 'Beneficial up to 1200ppm in controlled environments', '"CO2 in soil air and water"', 'Highly mobile', '', '["CO2 enrichment in greenhouses"]', 'All crops', '2026-06-26 15:48:13'),
    (2, 'Hydrogen', 'H', 'Non-mineral macronutrient', '', '["Component of all organic molecules", "Water transport", "pH regulation in cells"]', 'Hydrogen Deficiency', 'Wilting, leaf roll', '', '{}', '', 'Flooding conditions', '"H2O"', 'High', '', '["Irrigation water"]', 'All crops', '2026-06-26 15:48:13'),
    (3, 'Oxygen', 'O', 'Non-mineral macronutrient', '', '["Aerobic respiration", "Component of all organic molecules", "Root aeration"]', 'Oxygen Deficiency', 'Yellow leaves, root browning, sulfide smell', '', '{}', '', 'Not applicable', '"O2 in soil air"', 'High', '', '["Drainage improvement", "Raised beds"]', 'All crops, especially in waterlogged areas', '2026-06-26 15:48:13'),
    (4, 'Nitrogen', 'N', 'Primary Macronutrient', '1.5-4% dry weight', '["Component of amino acids, proteins, enzymes", "Chlorophyll synthesis (green color)", "Nucleic acid component (DNA, RNA)", "Promotes vegetative growth", "Enzyme activation"]', 'Nitrogen Deficiency (Chlorosis)', 'Pale yellow-green color starting from older leaves (lower); progresses upward; stunted growth; thin spindly stems; early maturity', 'Older/Lower leaves first (N is mobile, remobilized to young leaves)', '{"rice": "Pale yellow older leaves; reduced tillering; small, thin panicles", "maize": "Yellow stripe from tip of leaves (\"nitrogen streak\"), lower leaves yellow-brown", "wheat": "Pale green plants, purple tinting in some varieties, thin tillers", "tomato": "Light green plants, light purple tinting on stems"}', 'Dark green, lodging, delayed maturity, reduced grain quality, excessive vegetative growth, hollow stems', 'Varies widely by crop; depends on N form (ammonium vs nitrate)', '["Nitrate (NO3-) \u2014 mobile, leaches", "Ammonium (NH4+) \u2014 adsorbed on soil, less mobile", "Organic N \u2014 must mineralize first"]', 'Highly mobile — remobilized from old to young leaves', '6.0-7.0 (best mineralization)', '["Urea (46% N) \u2014 most common", "Ammonium Nitrate (34% N)", "Ammonium Sulphate (21% N, 24% S)", "Calcium Ammonium Nitrate (25% N)", "DAP (18% N, 46% P2O5)", "Legume green manure (biological fixation)", "FYM (0.5-1.5% N)"]', 'Rice, Wheat, Maize, Vegetables, Cotton', '2026-06-26 15:48:13'),
    (5, 'Phosphorus', 'P', 'Primary Macronutrient', '0.1-0.5% dry weight', '["Root development and growth", "Energy transfer (ATP, ADP)", "Nucleic acid component (DNA, RNA)", "Cell membrane phospholipids", "Early plant establishment and tillering", "Seed and fruit development"]', 'Phosphorus Deficiency (Purpling)', 'Dark green to purple/red color on older leaves and stems (anthocyanin accumulation); thin, weak roots; delayed maturity; small seeds', 'Older leaves first (P is mobile)', '{"maize": "Purple/red color on underside of leaves and stems \u2014 classic P deficiency sign", "tomato": "Purple undersides of leaves, bluish-green color, thin stems", "wheat": "Dark green to bluish, purple tinges, delayed maturity", "rice": "Thin, upright dark green or purple tinged leaves; reduced tillering"}', 'Zinc and iron deficiency symptoms (P-induced micronutrient deficiency); stunted growth when soil P very high', 'Soil Olsen P > 40ppm can induce Zn deficiency in some crops', '["Orthophosphate ions (H2PO4-, HPO42-) \u2014 plant-available", "Organic P \u2014 must mineralize", "Fixed P (Al, Fe, Ca phosphates) \u2014 unavailable"]', 'Mobile — remobilized from old to young tissue', '6.0-7.0', '["DAP \u2014 Diammonium Phosphate (46% P2O5, 18% N)", "SSP \u2014 Single Super Phosphate (16% P2O5, 11% S, 20% Ca)", "TSP \u2014 Triple Super Phosphate (46% P2O5)", "Rock Phosphate (28-35% P2O5) \u2014 slow release in acid soils", "Ammonium Polyphosphate", "Bone meal (20-25% P2O5)"]', 'All crops; especially legumes, root crops, cereals', '2026-06-26 15:48:13'),
    (6, 'Potassium', 'K', 'Primary Macronutrient', '1-4% dry weight', '["Stomatal regulation (drought resistance)", "Enzyme activation (>60 enzymes)", "Protein synthesis", "Disease resistance and strong cell walls", "Transport of sugars and nutrients in phloem", "Quality improvement (sugar content, fruit firmness, starch)"]', 'Potassium Deficiency (Potash Starvation)', 'Brown scorching and curling of leaf tips and margins (leaf scorch/marginal necrosis) starting on older leaves; brown spots inside leaf margin; weak stems; lodging in cereals', 'Older/Lower leaves first (K is mobile)', '{"potato": "Marginal necrosis on older leaves; small irregular tubers; reduced specific gravity", "banana": "Marginal leaf scorch, orange-yellow margins; bent leaf midribs; reduced bunch weight", "tomato": "Marginal leaf burn, blossom end rot aggravated; poor fruit color", "rice": "Brown spots on older leaves from tip, leaves with rusty-dark brown margins"}', 'Calcium and magnesium deficiency symptoms (K antagonism); salt effects in sandy soils', 'Soil K > 800 ppm can cause Mg deficiency in some crops', '["Exchangeable K (plant-available)", "Non-exchangeable K (in minerals \u2014 slowly available)", "Solution K (immediately available, small pool)"]', 'Highly mobile', '6.0-7.5', '["Muriate of Potash / MOP (60% K2O) \u2014 most common", "Sulphate of Potash / SOP (50% K2O, 18% S) \u2014 premium for Cl-sensitive crops", "Potassium Nitrate (44% K2O, 13% N) \u2014 for fertigation", "Potassium Chloride (KCl)", "Wood ash (5-10% K2O) \u2014 organic source"]', 'Potato, Banana, Sugarcane, Tobacco, Cotton, Tomato', '2026-06-26 15:48:13'),
    (7, 'Calcium', 'Ca', 'Secondary Macronutrient', '0.1-2% dry weight', '["Cell wall structure (calcium pectate in middle lamella)", "Cell membrane integrity", "Signal transduction", "Enzyme activation", "Root tip and young leaf development"]', 'Calcium Deficiency', 'Affects only new/young leaves and growing points (Ca is immobile); tip burn (leaf tips die), blossom end rot in tomato/pepper, bitter pit in apple, tip burn in lettuce and cabbage, hollow heart in brassica', 'Young/new leaves and growing points (Ca is IMMOBILE — not remobilized)', '{"tomato": "Blossom End Rot (BER) \u2014 dark leathery patch at fruit base", "apple": "Bitter pit \u2014 dark depressions/spots in flesh, internal browning", "lettuce": "Tip burn \u2014 marginal leaf necrosis", "potato": "Internal brown rust \u2014 discolored vascular tissue", "celery": "Blackheart \u2014 inner leaf death"}', 'Rare; reduces Mg, K, Zn uptake at very high Ca', 'pH > 8.0 with high Ca', '["Exchangeable Ca (most important)", "Solution Ca", "Mineral Ca (calcite, etc.)"]', 'Immobile — does not move from old to young tissue', '6.0-7.5 (Ca naturally adequate at these levels)', '["Agricultural Lime CaCO3 (36-40% Ca) \u2014 pH correction", "Dolomitic Lime \u2014 CaMg(CO3)2 \u2014 provides Ca + Mg", "Gypsum CaSO4 (23% Ca, 18% S) \u2014 for sodic soils; doesn''t raise pH", "Calcium Nitrate (19% Ca, 15.5% N) \u2014 for fertigation", "SSP (20% Ca, 16% P2O5)"]', 'Tomato, Pepper, Apple, Celery, Lettuce, Brassicas', '2026-06-26 15:48:13'),
    (8, 'Magnesium', 'Mg', 'Secondary Macronutrient', '0.05-0.5% dry weight', '["Central atom of chlorophyll molecule", "Enzyme activation (100+ enzymes)", "Phosphate transport within plant", "Sugar and protein synthesis", "Activates photosynthesis"]', 'Magnesium Deficiency (Interveinal Chlorosis)', 'Interveinal chlorosis on older leaves — yellowing between the veins while veins remain green; often starts as pale green, then yellow, then reddish-purple margins; leaves may curl upward', 'Older/Lower leaves first (Mg is mobile)', '{"apple": "Interveinal scorching of older leaves; premature defoliation", "maize": "Yellow/white stripes on older leaves, especially mid-rib area", "tomato": "Interveinal yellowing; older leaves affected; inside dark stripe on leaf", "sugarcane": "Yellow stripes on older leaves from tip to base"}', 'Rare outdoors; possible in greenhouse soils; reduces Ca uptake at very high Mg', '', '["Exchangeable Mg", "Solution Mg", "Mineral Mg (primary minerals)"]', 'Mobile', '6.0-7.0', '["Kieserite \u2014 Magnesium Sulphate (16% Mg, 22% S)", "Magnesium Sulphate (Epsom Salt) \u2014 (10% Mg) for foliar spray", "Dolomitic Lime \u2014 CaMg(CO3)2", "Magnesia (MgO)", "Langbeinite (K2Mg2(SO4)3)"]', 'Apple, Maize, Potato, Tomato, Grapes', '2026-06-26 15:48:13'),
    (9, 'Sulfur', 'S', 'Secondary Macronutrient', '0.05-0.5% dry weight', '["Component of amino acids (cysteine, methionine)", "Protein synthesis", "Enzyme cofactor", "Glucosinolate synthesis (brassicas)", "Chlorophyll synthesis support", "Flavor compounds in Alliums"]', 'Sulfur Deficiency', 'Interveinal chlorosis of YOUNG/NEW leaves (unlike Mg which affects old leaves) — pale yellow-green color of new leaves while old leaves remain green; stunted growth', 'Young/New leaves first (S is relatively immobile)', '{"brassica": "Cupping of leaves; pale yellow-green new leaves; reduced glucosinolate content", "onion": "Pale yellow-green young leaves; reduced pungency", "mustard": "Interveinal chlorosis of younger leaves", "oilpalm": "Chlorosis of leaflets; reduced yield"}', 'Sulfur toxicity rare in soils; atmospheric SO2 damage shows as leaf spots and margin burn', '', '["Sulphate ion SO42- (plant-available)", "Organic S (must mineralize)", "Pyritic S (in waterlogged soils)"]', 'Moderately mobile', '6.0-7.5', '["Ammonium Sulphate (24% S, 21% N)", "SSP (11% S)", "Kieserite (22% S, 16% Mg)", "Sulphate of Potash (18% S, 50% K2O)", "Gypsum CaSO4 (18% S)", "Wettable Sulfur (90-98% S) \u2014 fungicide + nutrient", "Elemental Sulfur (90-100% S) \u2014 acidifier, slow release"]', 'Onion, Garlic, Mustard, Canola, Sunflower, Sugarcane', '2026-06-26 15:48:13'),
    (10, 'Iron', 'Fe', 'Micronutrient', '50-300 ppm dry weight', '["Chlorophyll synthesis (not structural)", "Electron carrier in photosynthesis and respiration", "Enzyme cofactor (catalase, peroxidase)", "Nitrogen fixation in legumes", "Nitrate reduction"]', 'Iron Chlorosis (Lime-induced Chlorosis)', 'Interveinal chlorosis on YOUNG leaves — bright yellow leaves with dark green veins; in severe cases entire leaf turns yellow then white; known as ''lime-induced chlorosis'' on calcareous soils', 'Young/New leaves first (Fe is immobile)', '{"soybean": "Interveinal yellowing of new trifoliates; ''iron deficiency chlorosis (IDC)''", "groundnut": "Young leaf chlorosis in calcareous soils", "citrus": "Young leaf pale yellow with green veins \u2014 classic sign", "rice": "Iron toxicity (not deficiency) is common in acid waterlogged soils: bronzing of leaves"}', 'In waterlogged rice soils: bronze-brown speckling of leaf surface starting from tips; ''bronzing''; roots become brown and rotten; Reduced tillering', 'Fe > 300 ppm in plant tissue', '["Fe3+ (oxidized \u2014 insoluble in high pH soils)", "Fe2+ (reduced \u2014 soluble in waterlogged conditions)", "Fe chelates in organic matter"]', 'Immobile', '5.5-6.5 (best Fe availability)', '["FeSO4 (Iron Sulphate) \u2014 soil application 25-50 kg/ha", "Fe-EDTA, Fe-DTPA, Fe-EDDHA \u2014 chelated iron (most effective, especially at high pH)", "Fe-EDDHA \u2014 most stable in high pH soils (most expensive)", "Foliar spray: FeSO4 0.5-1% (5-10g/L)"]', 'Soybean, Groundnut, Citrus, Grapes, Sorghum (in calcareous soils)', '2026-06-26 15:48:13'),
    (11, 'Zinc', 'Zn', 'Micronutrient', '20-100 ppm dry weight', '["Enzyme activation (300+ enzymes)", "Auxin synthesis (growth hormone)", "Protein synthesis", "Chlorophyll formation", "Carbohydrate metabolism", "Pollen viability"]', 'Zinc Deficiency (Khaira Disease in Rice; Little Leaf in Fruits)', 'In cereals: pale brown spots on mid-leaf, interveinal chlorosis; In fruits: small leaves (little leaf), shortened internodes (rosetting); In maize: broad white/yellow bands (white bud); Rice: ''khaira disease'' — pale orange-brown blotching of older leaves', 'Older to young leaves depending on crop', '{"rice": "Khaira disease: brown rusty spots; reduced tillering; ''paddystraw'' leaves", "maize": "White bud: broad white band on leaf; severe growth stunting", "citrus": "Little leaf and rosette: small, narrow leaves; mottle leaf", "apple": "Rosette: shortened internodes; small mottled leaves"}', 'Root growth inhibition; interveinal chlorosis (Fe/Mn deficiency induced); common on contaminated soils', 'Plant Zn > 400 ppm is phytotoxic', '["Zn2+ ion (available)", "Organic complexes", "Zinc oxide, sulphide (insoluble at high pH)"]', 'Low mobility', '5.5-7.0', '["Zinc Sulphate Monohydrate (35% Zn) \u2014 most common; soil application 25 kg/ha", "Zinc Sulphate Heptahydrate (21% Zn)", "Zinc Oxide (80% Zn) \u2014 slow release", "Zinc Chelate (EDTA) \u2014 for fertigation", "Foliar spray: ZnSO4 0.5% + lime 0.25%", "Seed treatment: ZnSO4 solution soaking"]', 'Rice (Khaira), Maize (white bud), Citrus, Apple, Cotton, Legumes', '2026-06-26 15:48:13'),
    (12, 'Manganese', 'Mn', 'Micronutrient', '20-500 ppm dry weight', '["Photosystem II water splitting (oxygen evolution)", "Enzyme activation (Mn-SOD)", "Nitrogen assimilation", "Shikimate pathway (phenol synthesis)"]', 'Manganese Deficiency (Grey Speck in Oat; Pahala Blight in Sugarcane)', 'Interveinal chlorosis of younger leaves; grey-green patches between veins; tissue may remain light green with distinct green veins; eventually necrosis; oat: ''grey speck''; cereals: stripe patterns; sugarcane: ''pahala blight''', 'Young/New leaves first (Mn is immobile)', '{}', 'Brown speckling of older leaves, irregular brown spots; marginal necrosis; symptoms of Fe and Ca deficiency (Mn-induced); common in acid soils', 'Mn > 300 ppm in plant tissue; worst in acid soils (pH < 5.5)', '["Mn2+ (available \u2014 increases in acid/waterlogged soils)", "MnO2 (insoluble in alkaline, well-aerated soils)"]', 'Low', '', '["MnSO4 (32% Mn) \u2014 soil or foliar", "Mn chelates \u2014 for high pH soils", "Foliar spray: MnSO4 0.5% (5g/L)"]', 'Oat, Sugar Beet, Soybean, Legumes, Fruit trees', '2026-06-26 15:48:13'),
    (13, 'Boron', 'B', 'Micronutrient', '5-75 ppm dry weight', '["Cell wall structure (cross-links pectins)", "Reproduction (pollen tube growth, fertilization)", "Sugar translocation", "Calcium utilization", "Membrane integrity"]', 'Boron Deficiency (Hollow Heart, Heart Rot)', 'Death of growing points (apical meristem); distorted, thick, brittle, curled young leaves; hollow heart in beet/turnip; sunflower head sterility; poor fruit set; corky/cracked fruits; hollow stem in brassica', 'Young leaves and growing points (B is immobile)', '{"sunflower": "Hollow head: empty pith, no seeds formed", "cauliflower": "Brown curd, hollow stem", "apple": "Internal cork (brown cork-like tissue inside fruit)", "sugar_beet": "Heart rot: black necrosis of growing point"}', 'Marginal leaf burn of older leaves; yellow tips and margins; root damage; B has very narrow range between deficiency and toxicity', 'Foliar B > 200 ppm; soil > 2 ppm available B can be toxic to sensitive crops', '["Boric acid H3BO3 (main available form)", "Adsorbed B on clay and organic matter"]', 'Low (except in crops that synthesize sorbitol/mannitol)', '', '["Borax Na2B4O7.10H2O (11% B) \u2014 soil application 0.5-1 kg/ha", "Boric acid H3BO3 (17% B) \u2014 foliar spray 0.2-0.3%", "Solubor (20% B) \u2014 soluble for spraying", "Boron fertilizer granules \u2014 for mixed fertilizers"]', 'Sunflower, Brassicas, Sugar Beet, Apple, Groundnut, Cotton', '2026-06-26 15:48:13'),
    (14, 'Copper', 'Cu', 'Micronutrient', '2-20 ppm dry weight', '["Photosynthesis (plastocyanin)", "Enzyme activation (polyphenol oxidase, ascorbate oxidase)", "Lignin synthesis (cell wall strength)", "Pollen tube growth"]', 'Copper Deficiency (Reclamation Disease)', 'Wilting and dieback of growing tips (''die-back''); young leaves twisted, cup-shaped; pale blue-green color; in cereals: ''blind ear'' — twisted leaf sheaths preventing ear emergence; bluish-green hue', 'Young leaves and growing tips', '{}', 'Brown root discoloration; inhibited root growth; chlorosis; Fe deficiency symptoms', 'Soil Cu > 100 ppm is toxic to plants; vineyard soils with historical Bordeaux use are often Cu-toxic', '["Cu2+ and Cu+ ions (available)", "Organic Cu complexes (very stable)"]', 'Low', '', '["CuSO4 (25% Cu) \u2014 soil application 5-10 kg/ha", "Cu chelates", "Copper oxychloride (fungicide + nutrient)", "Foliar CuSO4 0.2% spray"]', 'Wheat, Oat, Rye, Spinach, Onion, Fruit trees on organic soils', '2026-06-26 15:48:13'),
    (15, 'Molybdenum', 'Mo', 'Micronutrient', '0.1-1 ppm dry weight', '["Nitrate reductase (NO3 to NH4 conversion)", "Nitrogen fixation in legumes (nitrogenase)", "Sulfite oxidase activity"]', 'Molybdenum Deficiency (Whiptail in Cauliflower)', 'Interveinal chlorosis of older leaves; ''whiptail'' in cauliflower/broccoli — leaves fail to unfurl properly, look like a whip; marginal scorch; in legumes: poor nodulation and N fixation', 'Young leaves in brassica; older leaves in other crops', '{}', 'Very rare; excess Mo causes Cu deficiency; plants may appear Cu-deficient', '', '["MoO42- (molybdate \u2014 available in neutral to alkaline soils)"]', '', '', '["Ammonium Molybdate (54% Mo) \u2014 tiny amounts needed 0.1-0.5 g/L foliar spray or seed treatment"]', 'Cauliflower, Broccoli, Legumes (for N fixation), Maize', '2026-06-26 15:48:13'),
    (16, 'Chlorine', 'Cl', 'Micronutrient', '100-10,000 ppm dry weight', '["Photosystem II water splitting", "Stomatal regulation", "Osmotic adjustment", "Disease suppression"]', 'Chlorine Deficiency (Very Rare)', 'Wilting; leaf bronzing; chlorosis; reduced growth — rarely seen in field crops as Cl is ubiquitous', 'Young leaves', '{}', 'Marginal leaf burn; bronze patches; premature leaf drop; salt stress symptoms', 'Soil ECe > 2 dS/m for sensitive crops', '["Cl- ion (mobile, easily leached)"]', '', '', '[]', 'Coconut (Cl responsive crop), Banana, Sugar Beet; Tobacco, Potato sensitive to Cl excess', '2026-06-26 15:48:13'),
    (17, 'Nickel', 'Ni', 'Micronutrient', '0.05-5 ppm dry weight', '["Urease enzyme component (urea breakdown)", "Nitrogen metabolism", "Seed germination and early vigor"]', 'Nickel Deficiency (Mouse Ear Disease in Pecan)', 'Accumulation of urea in leaf tips (tissue damage); ''mouse ear'' in pecan (small stunted rounded leaflets); leaf tip necrosis; poor seed viability', '', '{"pecan": "Mouse ear \u2014 small rounded deformed leaflets", "wheat": "Urea accumulation and necrotic leaf tips"}', 'Chlorosis; stunted growth; Fe deficiency induction; very toxic in acid soils', 'Soil Ni > 25 ppm phytotoxic', '[]', '', '', '["Nickel sulphate (very small amounts)"]', 'Pecan, Wheat, Legumes', '2026-06-26 15:48:13'),
    (18, 'Cobalt', 'Co', 'Beneficial Micronutrient (Legumes)', '0.01-0.5 ppm', '["Component of vitamin B12 in Rhizobium bacteria", "Essential for nitrogen fixation in legumes (indirect)", "Drought resistance"]', 'Cobalt Deficiency (affects legume N fixation)', 'Legumes: poor nodulation and N fixation; symptoms mimic N deficiency; pale green plants; mostly on severely leached or coarse-textured soils', '', '{"legumes": "Poor nodulation, yellowish small plants (like N deficiency)"}', '', '', '[]', '', '', '["CoSO4 at 0.1-0.2 kg/ha very small dose"]', 'Soybean, Clover, Alfalfa, Peanut (through Rhizobium)', '2026-06-26 15:48:13');

DROP TABLE IF EXISTS multilingual_names CASCADE;
CREATE TABLE multilingual_names (
    id INTEGER PRIMARY KEY NOT NULL,
    botanical_name VARCHAR(300) NOT NULL,
    language_code VARCHAR(10) NOT NULL,
    language_name VARCHAR(100) NULL,
    local_name VARCHAR(300) NOT NULL,
    script VARCHAR(50) NULL,
    created_at TIMESTAMP NULL
);

-- Data for multilingual_names (892 rows)
INSERT INTO multilingual_names (id, botanical_name, language_code, language_name, local_name, script, created_at) VALUES
    (1, 'Oryza sativa', 'en', 'English', 'Rice', 'Latin', '2026-06-26 15:48:13'),
    (2, 'Oryza sativa', 'hi', 'Hindi', 'Chawal / Dhan (धान)', 'Native', '2026-06-26 15:48:13'),
    (3, 'Oryza sativa', 'bn', 'Bengali', 'Dhaan (ধান)', 'Native', '2026-06-26 15:48:13'),
    (4, 'Oryza sativa', 'te', 'Telugu', 'Vadlu (వరి)', 'Native', '2026-06-26 15:48:13'),
    (5, 'Oryza sativa', 'ta', 'Tamil', 'Arisi (அரிசி)', 'Native', '2026-06-26 15:48:13'),
    (6, 'Oryza sativa', 'kn', 'Kannada', 'Akki (ಅಕ್ಕಿ)', 'Native', '2026-06-26 15:48:13'),
    (7, 'Oryza sativa', 'ml', 'Malayalam', 'Ari (അരി)', 'Native', '2026-06-26 15:48:13'),
    (8, 'Oryza sativa', 'mr', 'Marathi', 'Tandul (तांदूळ)', 'Native', '2026-06-26 15:48:13'),
    (9, 'Oryza sativa', 'pa', 'Punjabi', 'Jhona (ਝੋਨਾ)', 'Native', '2026-06-26 15:48:13'),
    (10, 'Oryza sativa', 'gu', 'Gujarati', 'Chaval', 'Native', '2026-06-26 15:48:13'),
    (11, 'Oryza sativa', 'or', 'Odia', 'Dhana (ଧାନ)', 'Native', '2026-06-26 15:48:13'),
    (12, 'Oryza sativa', 'as', 'Assamese', 'Dhan (ধান)', 'Native', '2026-06-26 15:48:13'),
    (13, 'Oryza sativa', 'ur', 'Urdu', 'Chawal (چاول)', 'Native', '2026-06-26 15:48:13'),
    (14, 'Oryza sativa', 'ar', 'Arabic', 'Arz (أرز)', 'Native', '2026-06-26 15:48:13'),
    (15, 'Oryza sativa', 'zh', 'Chinese (Mandarin)', 'Dào (稻)', 'Native', '2026-06-26 15:48:13'),
    (16, 'Oryza sativa', 'ja', 'Japanese', 'Kome (米)', 'Native', '2026-06-26 15:48:13'),
    (17, 'Oryza sativa', 'ko', 'Korean', 'Ssal (쌀)', 'Native', '2026-06-26 15:48:13'),
    (18, 'Oryza sativa', 'vi', 'Vietnamese', 'Lúa gạo', 'Latin', '2026-06-26 15:48:13'),
    (19, 'Oryza sativa', 'th', 'Thai', 'Khao (ข้าว)', 'Native', '2026-06-26 15:48:13'),
    (20, 'Oryza sativa', 'id', 'Indonesian', 'Padi', 'Latin', '2026-06-26 15:48:13'),
    (21, 'Oryza sativa', 'ms', 'Malay', 'Padi', 'Latin', '2026-06-26 15:48:13'),
    (22, 'Oryza sativa', 'tl', 'Filipino (Tagalog)', 'Palay', 'Latin', '2026-06-26 15:48:13'),
    (23, 'Oryza sativa', 'my', 'Burmese', 'Hsainn', 'Native', '2026-06-26 15:48:13'),
    (24, 'Oryza sativa', 'km', 'Khmer', 'Srov (ស្រូវ)', 'Native', '2026-06-26 15:48:13'),
    (25, 'Oryza sativa', 'si', 'Sinhala', 'Hal (හාල්)', 'Native', '2026-06-26 15:48:13'),
    (26, 'Oryza sativa', 'ne', 'Nepali', 'Chamal (चामल)', 'Native', '2026-06-26 15:48:13'),
    (27, 'Oryza sativa', 'sw', 'Swahili', 'Mchele', 'Latin', '2026-06-26 15:48:13'),
    (28, 'Oryza sativa', 'ha', 'Hausa', 'Shinkafa', 'Latin', '2026-06-26 15:48:13'),
    (29, 'Oryza sativa', 'yo', 'Yoruba', 'Iresi', 'Latin', '2026-06-26 15:48:13'),
    (30, 'Oryza sativa', 'ig', 'Igbo', 'Osikapa', 'Native', '2026-06-26 15:48:13'),
    (31, 'Oryza sativa', 'am', 'Amharic', 'Timhirt (ጤፍ)', 'Native', '2026-06-26 15:48:13'),
    (32, 'Oryza sativa', 'pt', 'Portuguese', 'Arroz', 'Latin', '2026-06-26 15:48:13'),
    (33, 'Oryza sativa', 'es', 'Spanish', 'Arroz', 'Latin', '2026-06-26 15:48:13'),
    (34, 'Oryza sativa', 'fr', 'French', 'Riz', 'Latin', '2026-06-26 15:48:13'),
    (35, 'Oryza sativa', 'de', 'German', 'Reis', 'Latin', '2026-06-26 15:48:13'),
    (36, 'Oryza sativa', 'it', 'Italian', 'Riso', 'Native', '2026-06-26 15:48:13'),
    (37, 'Oryza sativa', 'ru', 'Russian', 'Ris (рис)', 'Native', '2026-06-26 15:48:13'),
    (38, 'Oryza sativa', 'nl', 'Dutch', 'Rijst', 'Native', '2026-06-26 15:48:13'),
    (39, 'Oryza sativa', 'pl', 'Polish', 'Ryż', 'Native', '2026-06-26 15:48:13'),
    (40, 'Oryza sativa', 'tr', 'Turkish', 'Pirinç', 'Latin', '2026-06-26 15:48:13'),
    (41, 'Oryza sativa', 'fa', 'Persian (Farsi)', 'Berenj (برنج)', 'Native', '2026-06-26 15:48:13'),
    (42, 'Oryza sativa', 'kk', 'Kazakh', 'Küriş', 'Native', '2026-06-26 15:48:13'),
    (43, 'Oryza sativa', 'uz', 'Uzbek', 'Sholi', 'Native', '2026-06-26 15:48:13'),
    (44, 'Oryza sativa', 'tg', 'Tajik', 'Birinj', 'Native', '2026-06-26 15:48:13'),
    (45, 'Oryza sativa', 'ky', 'Kyrgyz', 'Küröch', 'Native', '2026-06-26 15:48:13'),
    (46, 'Triticum aestivum', 'en', 'English', 'Wheat', 'Latin', '2026-06-26 15:48:13'),
    (47, 'Triticum aestivum', 'hi', 'Hindi', 'Gehun (गेहूँ)', 'Native', '2026-06-26 15:48:13'),
    (48, 'Triticum aestivum', 'bn', 'Bengali', 'Gom (গম)', 'Native', '2026-06-26 15:48:13'),
    (49, 'Triticum aestivum', 'te', 'Telugu', 'Godhuma (గోధుమ)', 'Native', '2026-06-26 15:48:13'),
    (50, 'Triticum aestivum', 'ta', 'Tamil', 'Gothumai (கோதுமை)', 'Native', '2026-06-26 15:48:13'),
    (51, 'Triticum aestivum', 'kn', 'Kannada', 'Godi (ಗೋಧಿ)', 'Native', '2026-06-26 15:48:13'),
    (52, 'Triticum aestivum', 'ml', 'Malayalam', 'Gothambu (ഗോതമ്പ്)', 'Native', '2026-06-26 15:48:13'),
    (53, 'Triticum aestivum', 'mr', 'Marathi', 'Gahu (गहू)', 'Native', '2026-06-26 15:48:13'),
    (54, 'Triticum aestivum', 'pa', 'Punjabi', 'Kanak (ਕਣਕ)', 'Native', '2026-06-26 15:48:13'),
    (55, 'Triticum aestivum', 'gu', 'Gujarati', 'Ghaun (ઘઉ)', 'Native', '2026-06-26 15:48:13'),
    (56, 'Triticum aestivum', 'or', 'Odia', 'Gahama (ଗହମ)', 'Native', '2026-06-26 15:48:13'),
    (57, 'Triticum aestivum', 'as', 'Assamese', 'Gom (গম)', 'Native', '2026-06-26 15:48:13'),
    (58, 'Triticum aestivum', 'ur', 'Urdu', 'Gandum (گندم)', 'Native', '2026-06-26 15:48:13'),
    (59, 'Triticum aestivum', 'ar', 'Arabic', 'Qamh (قمح)', 'Native', '2026-06-26 15:48:13'),
    (60, 'Triticum aestivum', 'zh', 'Chinese (Mandarin)', 'Xiǎomài (小麦)', 'Native', '2026-06-26 15:48:13'),
    (61, 'Triticum aestivum', 'ja', 'Japanese', 'Komugi (小麦)', 'Native', '2026-06-26 15:48:13'),
    (62, 'Triticum aestivum', 'ko', 'Korean', 'Mil (밀)', 'Native', '2026-06-26 15:48:13'),
    (63, 'Triticum aestivum', 'vi', 'Vietnamese', 'Lúa mì', 'Latin', '2026-06-26 15:48:13'),
    (64, 'Triticum aestivum', 'th', 'Thai', 'Saalee (สาลี)', 'Native', '2026-06-26 15:48:13'),
    (65, 'Triticum aestivum', 'id', 'Indonesian', 'Gandum', 'Latin', '2026-06-26 15:48:13'),
    (66, 'Triticum aestivum', 'ms', 'Malay', 'Gandum', 'Latin', '2026-06-26 15:48:13'),
    (67, 'Triticum aestivum', 'tl', 'Filipino (Tagalog)', 'Trigo', 'Latin', '2026-06-26 15:48:13'),
    (68, 'Triticum aestivum', 'sw', 'Swahili', 'Ngano', 'Latin', '2026-06-26 15:48:13'),
    (69, 'Triticum aestivum', 'ha', 'Hausa', 'Alkama', 'Latin', '2026-06-26 15:48:13'),
    (70, 'Triticum aestivum', 'yo', 'Yoruba', 'Alikama', 'Latin', '2026-06-26 15:48:13'),
    (71, 'Triticum aestivum', 'am', 'Amharic', 'Senafich (ስንዴ)', 'Native', '2026-06-26 15:48:13'),
    (72, 'Triticum aestivum', 'pt', 'Portuguese', 'Trigo', 'Latin', '2026-06-26 15:48:13'),
    (73, 'Triticum aestivum', 'es', 'Spanish', 'Trigo', 'Latin', '2026-06-26 15:48:13'),
    (74, 'Triticum aestivum', 'fr', 'French', 'Blé', 'Latin', '2026-06-26 15:48:13'),
    (75, 'Triticum aestivum', 'de', 'German', 'Weizen', 'Latin', '2026-06-26 15:48:13'),
    (76, 'Triticum aestivum', 'it', 'Italian', 'Grano', 'Native', '2026-06-26 15:48:13'),
    (77, 'Triticum aestivum', 'ru', 'Russian', 'Pshenitsa (пшеница)', 'Native', '2026-06-26 15:48:13'),
    (78, 'Triticum aestivum', 'nl', 'Dutch', 'Tarwe', 'Native', '2026-06-26 15:48:13'),
    (79, 'Triticum aestivum', 'pl', 'Polish', 'Pszenica', 'Native', '2026-06-26 15:48:13'),
    (80, 'Triticum aestivum', 'tr', 'Turkish', 'Buğday', 'Latin', '2026-06-26 15:48:13'),
    (81, 'Triticum aestivum', 'fa', 'Persian (Farsi)', 'Gandom (گندم)', 'Native', '2026-06-26 15:48:13'),
    (82, 'Triticum aestivum', 'kk', 'Kazakh', 'Buday', 'Native', '2026-06-26 15:48:13'),
    (83, 'Triticum aestivum', 'uz', 'Uzbek', 'Bug''doy', 'Native', '2026-06-26 15:48:13'),
    (84, 'Triticum aestivum', 'ro', 'Romanian', 'Grâu', 'Native', '2026-06-26 15:48:13'),
    (85, 'Triticum aestivum', 'uk', 'Ukrainian', 'Pshenytsia (пшениця)', 'Native', '2026-06-26 15:48:13'),
    (86, 'Zea mays', 'en', 'English', 'Maize / Corn', 'Latin', '2026-06-26 15:48:13'),
    (87, 'Zea mays', 'hi', 'Hindi', 'Makka / Bhuta (मक्का)', 'Native', '2026-06-26 15:48:13'),
    (88, 'Zea mays', 'bn', 'Bengali', 'Bhutta (ভুট্টা)', 'Native', '2026-06-26 15:48:13'),
    (89, 'Zea mays', 'te', 'Telugu', 'Makka jowar (మొక్కజొన్న)', 'Native', '2026-06-26 15:48:13'),
    (90, 'Zea mays', 'ta', 'Tamil', 'Cholam (சோளம்)', 'Native', '2026-06-26 15:48:13'),
    (91, 'Zea mays', 'kn', 'Kannada', 'Jawari (ಜೋಳ)', 'Native', '2026-06-26 15:48:13'),
    (92, 'Zea mays', 'ml', 'Malayalam', 'Cholam (ചോളം)', 'Native', '2026-06-26 15:48:13'),
    (93, 'Zea mays', 'mr', 'Marathi', 'Makai (मका)', 'Native', '2026-06-26 15:48:13'),
    (94, 'Zea mays', 'pa', 'Punjabi', 'Makki (ਮੱਕੀ)', 'Native', '2026-06-26 15:48:13'),
    (95, 'Zea mays', 'gu', 'Gujarati', 'Makkai (મકાઈ)', 'Native', '2026-06-26 15:48:13'),
    (96, 'Zea mays', 'ur', 'Urdu', 'Makai (مکئی)', 'Native', '2026-06-26 15:48:13'),
    (97, 'Zea mays', 'ar', 'Arabic', 'Dhura (ذرة)', 'Native', '2026-06-26 15:48:13'),
    (98, 'Zea mays', 'zh', 'Chinese (Mandarin)', 'Yùmǐ (玉米)', 'Native', '2026-06-26 15:48:13'),
    (99, 'Zea mays', 'ja', 'Japanese', 'Tōmorokoshi (とうもろこし)', 'Native', '2026-06-26 15:48:13'),
    (100, 'Zea mays', 'ko', 'Korean', 'Oksusu (옥수수)', 'Native', '2026-06-26 15:48:13');
INSERT INTO multilingual_names (id, botanical_name, language_code, language_name, local_name, script, created_at) VALUES
    (101, 'Zea mays', 'vi', 'Vietnamese', 'Ngô', 'Latin', '2026-06-26 15:48:13'),
    (102, 'Zea mays', 'th', 'Thai', 'Khao Phot (ข้าวโพด)', 'Native', '2026-06-26 15:48:13'),
    (103, 'Zea mays', 'id', 'Indonesian', 'Jagung', 'Latin', '2026-06-26 15:48:13'),
    (104, 'Zea mays', 'ms', 'Malay', 'Jagung', 'Latin', '2026-06-26 15:48:13'),
    (105, 'Zea mays', 'tl', 'Filipino (Tagalog)', 'Mais', 'Latin', '2026-06-26 15:48:13'),
    (106, 'Zea mays', 'sw', 'Swahili', 'Mahindi', 'Latin', '2026-06-26 15:48:13'),
    (107, 'Zea mays', 'ha', 'Hausa', 'Masara', 'Latin', '2026-06-26 15:48:13'),
    (108, 'Zea mays', 'yo', 'Yoruba', 'Àgbàdo', 'Latin', '2026-06-26 15:48:13'),
    (109, 'Zea mays', 'ig', 'Igbo', 'Oka', 'Native', '2026-06-26 15:48:13'),
    (110, 'Zea mays', 'am', 'Amharic', 'Masara (ማሳር)', 'Native', '2026-06-26 15:48:13'),
    (111, 'Zea mays', 'pt', 'Portuguese', 'Milho', 'Latin', '2026-06-26 15:48:13'),
    (112, 'Zea mays', 'es', 'Spanish', 'Maíz', 'Latin', '2026-06-26 15:48:13'),
    (113, 'Zea mays', 'fr', 'French', 'Maïs', 'Latin', '2026-06-26 15:48:13'),
    (114, 'Zea mays', 'de', 'German', 'Mais', 'Latin', '2026-06-26 15:48:13'),
    (115, 'Zea mays', 'it', 'Italian', 'Granoturco', 'Native', '2026-06-26 15:48:13'),
    (116, 'Zea mays', 'ru', 'Russian', 'Kukuruza (кукуруза)', 'Native', '2026-06-26 15:48:13'),
    (117, 'Zea mays', 'nl', 'Dutch', 'Maïs', 'Native', '2026-06-26 15:48:13'),
    (118, 'Zea mays', 'pl', 'Polish', 'Kukurydza', 'Native', '2026-06-26 15:48:13'),
    (119, 'Zea mays', 'tr', 'Turkish', 'Mısır', 'Latin', '2026-06-26 15:48:13'),
    (120, 'Zea mays', 'fa', 'Persian (Farsi)', 'Zarat (ذرت)', 'Native', '2026-06-26 15:48:13'),
    (121, 'Zea mays', 'ro', 'Romanian', 'Porumb', 'Native', '2026-06-26 15:48:13'),
    (122, 'Zea mays', 'uk', 'Ukrainian', 'Kukurudza (кукурудза)', 'Native', '2026-06-26 15:48:13'),
    (123, 'Mangifera indica', 'en', 'English', 'Mango', 'Latin', '2026-06-26 15:48:13'),
    (124, 'Mangifera indica', 'hi', 'Hindi', 'Aam (आम)', 'Native', '2026-06-26 15:48:13'),
    (125, 'Mangifera indica', 'bn', 'Bengali', 'Aam (আম)', 'Native', '2026-06-26 15:48:13'),
    (126, 'Mangifera indica', 'te', 'Telugu', 'Mamidi (మామిడి)', 'Native', '2026-06-26 15:48:13'),
    (127, 'Mangifera indica', 'ta', 'Tamil', 'Maambalam (மாம்பழம்)', 'Native', '2026-06-26 15:48:13'),
    (128, 'Mangifera indica', 'kn', 'Kannada', 'Mavina Hannu (ಮಾವಿನ ಹಣ್ಣು)', 'Native', '2026-06-26 15:48:13'),
    (129, 'Mangifera indica', 'ml', 'Malayalam', 'Mampazham (മാമ്പഴം)', 'Native', '2026-06-26 15:48:13'),
    (130, 'Mangifera indica', 'mr', 'Marathi', 'Amba (आंबा)', 'Native', '2026-06-26 15:48:13'),
    (131, 'Mangifera indica', 'pa', 'Punjabi', 'Aam (ਅੰਬ)', 'Native', '2026-06-26 15:48:13'),
    (132, 'Mangifera indica', 'gu', 'Gujarati', 'Keri (કેરી)', 'Native', '2026-06-26 15:48:13'),
    (133, 'Mangifera indica', 'ur', 'Urdu', 'Aam (آم)', 'Native', '2026-06-26 15:48:13'),
    (134, 'Mangifera indica', 'ar', 'Arabic', 'Manga (مانجو)', 'Native', '2026-06-26 15:48:13'),
    (135, 'Mangifera indica', 'zh', 'Chinese (Mandarin)', 'Mángguǒ (芒果)', 'Native', '2026-06-26 15:48:13'),
    (136, 'Mangifera indica', 'ja', 'Japanese', 'Mango (マンゴー)', 'Native', '2026-06-26 15:48:13'),
    (137, 'Mangifera indica', 'ko', 'Korean', 'Manggo (망고)', 'Native', '2026-06-26 15:48:13'),
    (138, 'Mangifera indica', 'vi', 'Vietnamese', 'Xoài', 'Latin', '2026-06-26 15:48:13'),
    (139, 'Mangifera indica', 'th', 'Thai', 'Mamuang (มะม่วง)', 'Native', '2026-06-26 15:48:13'),
    (140, 'Mangifera indica', 'id', 'Indonesian', 'Mangga', 'Latin', '2026-06-26 15:48:13'),
    (141, 'Mangifera indica', 'ms', 'Malay', 'Mangga', 'Latin', '2026-06-26 15:48:13'),
    (142, 'Mangifera indica', 'tl', 'Filipino (Tagalog)', 'Mangga', 'Latin', '2026-06-26 15:48:13'),
    (143, 'Mangifera indica', 'my', 'Burmese', 'Thayet', 'Native', '2026-06-26 15:48:13'),
    (144, 'Mangifera indica', 'sw', 'Swahili', 'Embe', 'Latin', '2026-06-26 15:48:13'),
    (145, 'Mangifera indica', 'ha', 'Hausa', 'Mangwaro', 'Latin', '2026-06-26 15:48:13'),
    (146, 'Mangifera indica', 'pt', 'Portuguese', 'Manga', 'Latin', '2026-06-26 15:48:13'),
    (147, 'Mangifera indica', 'es', 'Spanish', 'Mango', 'Latin', '2026-06-26 15:48:13'),
    (148, 'Mangifera indica', 'fr', 'French', 'Mangue', 'Latin', '2026-06-26 15:48:13'),
    (149, 'Mangifera indica', 'de', 'German', 'Mango', 'Latin', '2026-06-26 15:48:13'),
    (150, 'Mangifera indica', 'it', 'Italian', 'Mango', 'Native', '2026-06-26 15:48:13'),
    (151, 'Mangifera indica', 'ru', 'Russian', 'Mango (манго)', 'Native', '2026-06-26 15:48:13'),
    (152, 'Mangifera indica', 'tr', 'Turkish', 'Mango', 'Latin', '2026-06-26 15:48:13'),
    (153, 'Musa acuminata', 'en', 'English', 'Banana', 'Latin', '2026-06-26 15:48:13'),
    (154, 'Musa acuminata', 'hi', 'Hindi', 'Kela (केला)', 'Native', '2026-06-26 15:48:13'),
    (155, 'Musa acuminata', 'bn', 'Bengali', 'Kola (কলা)', 'Native', '2026-06-26 15:48:13'),
    (156, 'Musa acuminata', 'te', 'Telugu', 'Arati Pandu (అరటిపండు)', 'Native', '2026-06-26 15:48:13'),
    (157, 'Musa acuminata', 'ta', 'Tamil', 'Vazhai Pazham (வாழைப்பழம்)', 'Native', '2026-06-26 15:48:13'),
    (158, 'Musa acuminata', 'kn', 'Kannada', 'Bale Hannu (ಬಾಳೆ ಹಣ್ಣು)', 'Native', '2026-06-26 15:48:13'),
    (159, 'Musa acuminata', 'ml', 'Malayalam', 'Vazha Pazham (വാഴ്ചഫലം)', 'Native', '2026-06-26 15:48:13'),
    (160, 'Musa acuminata', 'mr', 'Marathi', 'Keli (केळी)', 'Native', '2026-06-26 15:48:13'),
    (161, 'Musa acuminata', 'pa', 'Punjabi', 'Kela (ਕੇਲਾ)', 'Native', '2026-06-26 15:48:13'),
    (162, 'Musa acuminata', 'gu', 'Gujarati', 'Kela (કેળ)', 'Native', '2026-06-26 15:48:13'),
    (163, 'Musa acuminata', 'ur', 'Urdu', 'Kela (کیلا)', 'Native', '2026-06-26 15:48:13'),
    (164, 'Musa acuminata', 'ar', 'Arabic', 'Mouz (موز)', 'Native', '2026-06-26 15:48:13'),
    (165, 'Musa acuminata', 'zh', 'Chinese (Mandarin)', 'Xiāngjiāo (香蕉)', 'Native', '2026-06-26 15:48:13'),
    (166, 'Musa acuminata', 'ja', 'Japanese', 'Banana (バナナ)', 'Native', '2026-06-26 15:48:13'),
    (167, 'Musa acuminata', 'ko', 'Korean', 'Banana (바나나)', 'Native', '2026-06-26 15:48:13'),
    (168, 'Musa acuminata', 'vi', 'Vietnamese', 'Chuối', 'Latin', '2026-06-26 15:48:13'),
    (169, 'Musa acuminata', 'th', 'Thai', 'Kluai (กล้วย)', 'Native', '2026-06-26 15:48:13'),
    (170, 'Musa acuminata', 'id', 'Indonesian', 'Pisang', 'Latin', '2026-06-26 15:48:13'),
    (171, 'Musa acuminata', 'ms', 'Malay', 'Pisang', 'Latin', '2026-06-26 15:48:13'),
    (172, 'Musa acuminata', 'tl', 'Filipino (Tagalog)', 'Saging', 'Latin', '2026-06-26 15:48:13'),
    (173, 'Musa acuminata', 'sw', 'Swahili', 'Ndizi', 'Latin', '2026-06-26 15:48:13'),
    (174, 'Musa acuminata', 'ha', 'Hausa', 'Ayaba', 'Latin', '2026-06-26 15:48:13'),
    (175, 'Musa acuminata', 'yo', 'Yoruba', 'Ọgẹdẹ', 'Latin', '2026-06-26 15:48:13'),
    (176, 'Musa acuminata', 'pt', 'Portuguese', 'Banana', 'Latin', '2026-06-26 15:48:13'),
    (177, 'Musa acuminata', 'es', 'Spanish', 'Banana/Plátano', 'Latin', '2026-06-26 15:48:13'),
    (178, 'Musa acuminata', 'fr', 'French', 'Banane', 'Latin', '2026-06-26 15:48:13'),
    (179, 'Musa acuminata', 'de', 'German', 'Banane', 'Latin', '2026-06-26 15:48:13'),
    (180, 'Musa acuminata', 'it', 'Italian', 'Banana', 'Native', '2026-06-26 15:48:13'),
    (181, 'Musa acuminata', 'ru', 'Russian', 'Banan (банан)', 'Native', '2026-06-26 15:48:13'),
    (182, 'Solanum lycopersicum', 'en', 'English', 'Tomato', 'Latin', '2026-06-26 15:48:13'),
    (183, 'Solanum lycopersicum', 'hi', 'Hindi', 'Tamatar (टमाटर)', 'Native', '2026-06-26 15:48:13'),
    (184, 'Solanum lycopersicum', 'bn', 'Bengali', 'Tomato (টমেটো)', 'Native', '2026-06-26 15:48:13'),
    (185, 'Solanum lycopersicum', 'te', 'Telugu', 'Tomato (టమాటా)', 'Native', '2026-06-26 15:48:13'),
    (186, 'Solanum lycopersicum', 'ta', 'Tamil', 'Thakkali (தக்காளி)', 'Native', '2026-06-26 15:48:13'),
    (187, 'Solanum lycopersicum', 'kn', 'Kannada', 'Tomato (ಟಮೇಟ)', 'Native', '2026-06-26 15:48:13'),
    (188, 'Solanum lycopersicum', 'ml', 'Malayalam', 'Thakkali (തക്കാളി)', 'Native', '2026-06-26 15:48:13'),
    (189, 'Solanum lycopersicum', 'mr', 'Marathi', 'Tomato (टोमॅटो)', 'Native', '2026-06-26 15:48:13'),
    (190, 'Solanum lycopersicum', 'pa', 'Punjabi', 'Tamater (ਟਮਾਟਰ)', 'Native', '2026-06-26 15:48:13'),
    (191, 'Solanum lycopersicum', 'gu', 'Gujarati', 'Tameta (ટામેટું)', 'Native', '2026-06-26 15:48:13'),
    (192, 'Solanum lycopersicum', 'ur', 'Urdu', 'Tamatar (ٹماٹر)', 'Native', '2026-06-26 15:48:13'),
    (193, 'Solanum lycopersicum', 'ar', 'Arabic', 'Tamatim (طماطم)', 'Native', '2026-06-26 15:48:13'),
    (194, 'Solanum lycopersicum', 'zh', 'Chinese (Mandarin)', 'Xīhóngshì (西红柿)', 'Native', '2026-06-26 15:48:13'),
    (195, 'Solanum lycopersicum', 'ja', 'Japanese', 'Tomato (トマト)', 'Native', '2026-06-26 15:48:13'),
    (196, 'Solanum lycopersicum', 'ko', 'Korean', 'Tomato (토마토)', 'Native', '2026-06-26 15:48:13'),
    (197, 'Solanum lycopersicum', 'vi', 'Vietnamese', 'Cà chua', 'Latin', '2026-06-26 15:48:13'),
    (198, 'Solanum lycopersicum', 'th', 'Thai', 'Makhua thet (มะเขือเทศ)', 'Native', '2026-06-26 15:48:13'),
    (199, 'Solanum lycopersicum', 'id', 'Indonesian', 'Tomat', 'Latin', '2026-06-26 15:48:13'),
    (200, 'Solanum lycopersicum', 'ms', 'Malay', 'Tomato', 'Latin', '2026-06-26 15:48:13');
INSERT INTO multilingual_names (id, botanical_name, language_code, language_name, local_name, script, created_at) VALUES
    (201, 'Solanum lycopersicum', 'tl', 'Filipino (Tagalog)', 'Kamatis', 'Latin', '2026-06-26 15:48:13'),
    (202, 'Solanum lycopersicum', 'sw', 'Swahili', 'Nyanya', 'Latin', '2026-06-26 15:48:13'),
    (203, 'Solanum lycopersicum', 'ha', 'Hausa', 'Tumatir', 'Latin', '2026-06-26 15:48:13'),
    (204, 'Solanum lycopersicum', 'yo', 'Yoruba', 'Tomáti', 'Latin', '2026-06-26 15:48:13'),
    (205, 'Solanum lycopersicum', 'pt', 'Portuguese', 'Tomate', 'Latin', '2026-06-26 15:48:13'),
    (206, 'Solanum lycopersicum', 'es', 'Spanish', 'Tomate', 'Latin', '2026-06-26 15:48:13'),
    (207, 'Solanum lycopersicum', 'fr', 'French', 'Tomate', 'Latin', '2026-06-26 15:48:13'),
    (208, 'Solanum lycopersicum', 'de', 'German', 'Tomate', 'Latin', '2026-06-26 15:48:13'),
    (209, 'Solanum lycopersicum', 'it', 'Italian', 'Pomodoro', 'Native', '2026-06-26 15:48:13'),
    (210, 'Solanum lycopersicum', 'ru', 'Russian', 'Pomidor (помидор)', 'Native', '2026-06-26 15:48:13'),
    (211, 'Solanum lycopersicum', 'tr', 'Turkish', 'Domates', 'Latin', '2026-06-26 15:48:13'),
    (212, 'Solanum lycopersicum', 'nl', 'Dutch', 'Tomaat', 'Native', '2026-06-26 15:48:13'),
    (213, 'Solanum lycopersicum', 'pl', 'Polish', 'Pomidor', 'Native', '2026-06-26 15:48:13'),
    (214, 'Solanum lycopersicum', 'ro', 'Romanian', 'Roșie', 'Native', '2026-06-26 15:48:13'),
    (215, 'Solanum tuberosum', 'en', 'English', 'Potato', 'Latin', '2026-06-26 15:48:13'),
    (216, 'Solanum tuberosum', 'hi', 'Hindi', 'Aloo (आलू)', 'Native', '2026-06-26 15:48:13'),
    (217, 'Solanum tuberosum', 'bn', 'Bengali', 'Aloo (আলু)', 'Native', '2026-06-26 15:48:13'),
    (218, 'Solanum tuberosum', 'te', 'Telugu', 'Uralagedda (ఉరుళగడ్డ)', 'Native', '2026-06-26 15:48:13'),
    (219, 'Solanum tuberosum', 'ta', 'Tamil', 'Urulaikizhangu (உருளைக்கிழங்கு)', 'Native', '2026-06-26 15:48:13'),
    (220, 'Solanum tuberosum', 'kn', 'Kannada', 'Alu Gedde (ಆಲೂ ಗಡ್ಡೆ)', 'Native', '2026-06-26 15:48:13'),
    (221, 'Solanum tuberosum', 'ml', 'Malayalam', 'Urulakkizhangu (ഉരുളക്കിഴങ്ങ്)', 'Native', '2026-06-26 15:48:13'),
    (222, 'Solanum tuberosum', 'mr', 'Marathi', 'Batata (बटाटा)', 'Native', '2026-06-26 15:48:13'),
    (223, 'Solanum tuberosum', 'pa', 'Punjabi', 'Aloo (ਆਲੂ)', 'Native', '2026-06-26 15:48:13'),
    (224, 'Solanum tuberosum', 'gu', 'Gujarati', 'Bataka (બટેટા)', 'Native', '2026-06-26 15:48:13'),
    (225, 'Solanum tuberosum', 'ur', 'Urdu', 'Aloo (آلو)', 'Native', '2026-06-26 15:48:13'),
    (226, 'Solanum tuberosum', 'ar', 'Arabic', 'Batata (بطاطس)', 'Native', '2026-06-26 15:48:13'),
    (227, 'Solanum tuberosum', 'zh', 'Chinese (Mandarin)', 'Tǔdòu (土豆)', 'Native', '2026-06-26 15:48:13'),
    (228, 'Solanum tuberosum', 'ja', 'Japanese', 'Jagaimo (じゃがいも)', 'Native', '2026-06-26 15:48:13'),
    (229, 'Solanum tuberosum', 'ko', 'Korean', 'Gamja (감자)', 'Native', '2026-06-26 15:48:13'),
    (230, 'Solanum tuberosum', 'vi', 'Vietnamese', 'Khoai tây', 'Latin', '2026-06-26 15:48:13'),
    (231, 'Solanum tuberosum', 'th', 'Thai', 'Man farang (มันฝรั่ง)', 'Native', '2026-06-26 15:48:13'),
    (232, 'Solanum tuberosum', 'id', 'Indonesian', 'Kentang', 'Latin', '2026-06-26 15:48:13'),
    (233, 'Solanum tuberosum', 'ms', 'Malay', 'Kentang', 'Latin', '2026-06-26 15:48:13'),
    (234, 'Solanum tuberosum', 'tl', 'Filipino (Tagalog)', 'Patatas', 'Latin', '2026-06-26 15:48:13'),
    (235, 'Solanum tuberosum', 'sw', 'Swahili', 'Kiazi', 'Latin', '2026-06-26 15:48:13'),
    (236, 'Solanum tuberosum', 'ha', 'Hausa', 'Dankali', 'Latin', '2026-06-26 15:48:13'),
    (237, 'Solanum tuberosum', 'yo', 'Yoruba', 'Ànàmò', 'Latin', '2026-06-26 15:48:13'),
    (238, 'Solanum tuberosum', 'pt', 'Portuguese', 'Batata', 'Latin', '2026-06-26 15:48:13'),
    (239, 'Solanum tuberosum', 'es', 'Spanish', 'Patata/Papa', 'Latin', '2026-06-26 15:48:13'),
    (240, 'Solanum tuberosum', 'fr', 'French', 'Pomme de terre', 'Latin', '2026-06-26 15:48:13'),
    (241, 'Solanum tuberosum', 'de', 'German', 'Kartoffel', 'Latin', '2026-06-26 15:48:13'),
    (242, 'Solanum tuberosum', 'it', 'Italian', 'Patata', 'Native', '2026-06-26 15:48:13'),
    (243, 'Solanum tuberosum', 'ru', 'Russian', 'Kartofel (картофель)', 'Native', '2026-06-26 15:48:13'),
    (244, 'Solanum tuberosum', 'nl', 'Dutch', 'Aardappel', 'Native', '2026-06-26 15:48:13'),
    (245, 'Solanum tuberosum', 'pl', 'Polish', 'Ziemniak', 'Native', '2026-06-26 15:48:13'),
    (246, 'Solanum tuberosum', 'tr', 'Turkish', 'Patates', 'Latin', '2026-06-26 15:48:13'),
    (247, 'Allium cepa', 'en', 'English', 'Onion', 'Latin', '2026-06-26 15:48:13'),
    (248, 'Allium cepa', 'hi', 'Hindi', 'Pyaz (प्याज)', 'Native', '2026-06-26 15:48:13'),
    (249, 'Allium cepa', 'bn', 'Bengali', 'Peyaj (পেঁয়াজ)', 'Native', '2026-06-26 15:48:13'),
    (250, 'Allium cepa', 'te', 'Telugu', 'Nirulli (నిరుల్లి)', 'Native', '2026-06-26 15:48:13'),
    (251, 'Allium cepa', 'ta', 'Tamil', 'Vengayam (வெங்காயம்)', 'Native', '2026-06-26 15:48:13'),
    (252, 'Allium cepa', 'kn', 'Kannada', 'Irulli (ಈರುಳ್ಳಿ)', 'Native', '2026-06-26 15:48:13'),
    (253, 'Allium cepa', 'ml', 'Malayalam', 'Ulli (ഉള്ളി)', 'Native', '2026-06-26 15:48:13'),
    (254, 'Allium cepa', 'mr', 'Marathi', 'Kanda (कांदा)', 'Native', '2026-06-26 15:48:13'),
    (255, 'Allium cepa', 'pa', 'Punjabi', 'Piyaz (ਪਿਆਜ਼)', 'Native', '2026-06-26 15:48:13'),
    (256, 'Allium cepa', 'gu', 'Gujarati', 'Dungri (ડુંગળી)', 'Native', '2026-06-26 15:48:13'),
    (257, 'Allium cepa', 'ur', 'Urdu', 'Piyaz (پیاز)', 'Native', '2026-06-26 15:48:13'),
    (258, 'Allium cepa', 'ar', 'Arabic', 'Basal (بصل)', 'Native', '2026-06-26 15:48:13'),
    (259, 'Allium cepa', 'zh', 'Chinese (Mandarin)', 'Yángcōng (洋葱)', 'Native', '2026-06-26 15:48:13'),
    (260, 'Allium cepa', 'ja', 'Japanese', 'Tamanegi (玉ねぎ)', 'Native', '2026-06-26 15:48:13'),
    (261, 'Allium cepa', 'ko', 'Korean', 'Yangpa (양파)', 'Native', '2026-06-26 15:48:13'),
    (262, 'Allium cepa', 'vi', 'Vietnamese', 'Hành tây', 'Latin', '2026-06-26 15:48:13'),
    (263, 'Allium cepa', 'th', 'Thai', 'Hua hom (หัวหอม)', 'Native', '2026-06-26 15:48:13'),
    (264, 'Allium cepa', 'id', 'Indonesian', 'Bawang merah', 'Latin', '2026-06-26 15:48:13'),
    (265, 'Allium cepa', 'ms', 'Malay', 'Bawang', 'Latin', '2026-06-26 15:48:13'),
    (266, 'Allium cepa', 'tl', 'Filipino (Tagalog)', 'Sibuyas', 'Latin', '2026-06-26 15:48:13'),
    (267, 'Allium cepa', 'sw', 'Swahili', 'Kitunguu', 'Latin', '2026-06-26 15:48:13'),
    (268, 'Allium cepa', 'ha', 'Hausa', 'Albasa', 'Latin', '2026-06-26 15:48:13'),
    (269, 'Allium cepa', 'yo', 'Yoruba', 'Àlùbọ́sà', 'Latin', '2026-06-26 15:48:13'),
    (270, 'Allium cepa', 'pt', 'Portuguese', 'Cebola', 'Latin', '2026-06-26 15:48:13'),
    (271, 'Allium cepa', 'es', 'Spanish', 'Cebolla', 'Latin', '2026-06-26 15:48:13'),
    (272, 'Allium cepa', 'fr', 'French', 'Oignon', 'Latin', '2026-06-26 15:48:13'),
    (273, 'Allium cepa', 'de', 'German', 'Zwiebel', 'Latin', '2026-06-26 15:48:13'),
    (274, 'Allium cepa', 'it', 'Italian', 'Cipolla', 'Native', '2026-06-26 15:48:13'),
    (275, 'Allium cepa', 'ru', 'Russian', 'Luk (лук)', 'Native', '2026-06-26 15:48:13'),
    (276, 'Allium cepa', 'tr', 'Turkish', 'Soğan', 'Latin', '2026-06-26 15:48:13'),
    (277, 'Allium sativum', 'en', 'English', 'Garlic', 'Latin', '2026-06-26 15:48:13'),
    (278, 'Allium sativum', 'hi', 'Hindi', 'Lahsun (लहसुन)', 'Native', '2026-06-26 15:48:13'),
    (279, 'Allium sativum', 'bn', 'Bengali', 'Rasun (রসুন)', 'Native', '2026-06-26 15:48:13'),
    (280, 'Allium sativum', 'te', 'Telugu', 'Vellulli (వెల్లుల్లి)', 'Native', '2026-06-26 15:48:13'),
    (281, 'Allium sativum', 'ta', 'Tamil', 'Poondu (பூண்டு)', 'Native', '2026-06-26 15:48:13'),
    (282, 'Allium sativum', 'kn', 'Kannada', 'Bellulli (ಬೆಳ್ಳುಳ್ಳಿ)', 'Native', '2026-06-26 15:48:13'),
    (283, 'Allium sativum', 'ml', 'Malayalam', 'Veluthulli (വെളുത്തുള്ളി)', 'Native', '2026-06-26 15:48:13'),
    (284, 'Allium sativum', 'mr', 'Marathi', 'Lasun (लसूण)', 'Native', '2026-06-26 15:48:13'),
    (285, 'Allium sativum', 'pa', 'Punjabi', 'Thum (ਥੁੰਮ)', 'Native', '2026-06-26 15:48:13'),
    (286, 'Allium sativum', 'gu', 'Gujarati', 'Lasan (લ‌સણ)', 'Native', '2026-06-26 15:48:13'),
    (287, 'Allium sativum', 'ur', 'Urdu', 'Lahsun (لہسن)', 'Native', '2026-06-26 15:48:13'),
    (288, 'Allium sativum', 'ar', 'Arabic', 'Thoum (ثوم)', 'Native', '2026-06-26 15:48:13'),
    (289, 'Allium sativum', 'zh', 'Chinese (Mandarin)', 'Dàsuàn (大蒜)', 'Native', '2026-06-26 15:48:13'),
    (290, 'Allium sativum', 'ja', 'Japanese', 'Ninniku (にんにく)', 'Native', '2026-06-26 15:48:13'),
    (291, 'Allium sativum', 'ko', 'Korean', 'Maneul (마늘)', 'Native', '2026-06-26 15:48:13'),
    (292, 'Allium sativum', 'vi', 'Vietnamese', 'Tỏi', 'Latin', '2026-06-26 15:48:13'),
    (293, 'Allium sativum', 'th', 'Thai', 'Kratiam (กระเทียม)', 'Native', '2026-06-26 15:48:13'),
    (294, 'Allium sativum', 'id', 'Indonesian', 'Bawang putih', 'Latin', '2026-06-26 15:48:13'),
    (295, 'Allium sativum', 'ms', 'Malay', 'Bawang putih', 'Latin', '2026-06-26 15:48:13'),
    (296, 'Allium sativum', 'tl', 'Filipino (Tagalog)', 'Bawang', 'Latin', '2026-06-26 15:48:13'),
    (297, 'Allium sativum', 'sw', 'Swahili', 'Kitunguu saumu', 'Latin', '2026-06-26 15:48:13'),
    (298, 'Allium sativum', 'yo', 'Yoruba', 'Àjọ̀', 'Latin', '2026-06-26 15:48:13'),
    (299, 'Allium sativum', 'pt', 'Portuguese', 'Alho', 'Latin', '2026-06-26 15:48:13'),
    (300, 'Allium sativum', 'es', 'Spanish', 'Ajo', 'Latin', '2026-06-26 15:48:13');
INSERT INTO multilingual_names (id, botanical_name, language_code, language_name, local_name, script, created_at) VALUES
    (301, 'Allium sativum', 'fr', 'French', 'Ail', 'Latin', '2026-06-26 15:48:13'),
    (302, 'Allium sativum', 'de', 'German', 'Knoblauch', 'Latin', '2026-06-26 15:48:13'),
    (303, 'Allium sativum', 'it', 'Italian', 'Aglio', 'Native', '2026-06-26 15:48:13'),
    (304, 'Allium sativum', 'ru', 'Russian', 'Chesnok (чеснок)', 'Native', '2026-06-26 15:48:13'),
    (305, 'Allium sativum', 'tr', 'Turkish', 'Sarımsak', 'Latin', '2026-06-26 15:48:13'),
    (306, 'Zingiber officinale', 'en', 'English', 'Ginger', 'Latin', '2026-06-26 15:48:13'),
    (307, 'Zingiber officinale', 'hi', 'Hindi', 'Adrak (अदरक)', 'Native', '2026-06-26 15:48:13'),
    (308, 'Zingiber officinale', 'bn', 'Bengali', 'Aada (আদা)', 'Native', '2026-06-26 15:48:13'),
    (309, 'Zingiber officinale', 'te', 'Telugu', 'Allam (అల్లం)', 'Native', '2026-06-26 15:48:13'),
    (310, 'Zingiber officinale', 'ta', 'Tamil', 'Inji (இஞ்சி)', 'Native', '2026-06-26 15:48:13'),
    (311, 'Zingiber officinale', 'kn', 'Kannada', 'Shunti (ಶುಂಠಿ)', 'Native', '2026-06-26 15:48:13'),
    (312, 'Zingiber officinale', 'ml', 'Malayalam', 'Inji (ഇഞ്ചി)', 'Native', '2026-06-26 15:48:13'),
    (313, 'Zingiber officinale', 'mr', 'Marathi', 'Ale (आले)', 'Native', '2026-06-26 15:48:13'),
    (314, 'Zingiber officinale', 'pa', 'Punjabi', 'Adrak (ਅਦਰਕ)', 'Native', '2026-06-26 15:48:13'),
    (315, 'Zingiber officinale', 'gu', 'Gujarati', 'Aadu (આદુ)', 'Native', '2026-06-26 15:48:13'),
    (316, 'Zingiber officinale', 'ur', 'Urdu', 'Adrak (ادرک)', 'Native', '2026-06-26 15:48:13'),
    (317, 'Zingiber officinale', 'ar', 'Arabic', 'Zanjabil (زنجبيل)', 'Native', '2026-06-26 15:48:13'),
    (318, 'Zingiber officinale', 'zh', 'Chinese (Mandarin)', 'Jiāng (姜)', 'Native', '2026-06-26 15:48:13'),
    (319, 'Zingiber officinale', 'ja', 'Japanese', 'Shōga (しょうが)', 'Native', '2026-06-26 15:48:13'),
    (320, 'Zingiber officinale', 'ko', 'Korean', 'Saenggang (생강)', 'Native', '2026-06-26 15:48:13'),
    (321, 'Zingiber officinale', 'vi', 'Vietnamese', 'Gừng', 'Latin', '2026-06-26 15:48:13'),
    (322, 'Zingiber officinale', 'th', 'Thai', 'Khing (ขิง)', 'Native', '2026-06-26 15:48:13'),
    (323, 'Zingiber officinale', 'id', 'Indonesian', 'Jahe', 'Latin', '2026-06-26 15:48:13'),
    (324, 'Zingiber officinale', 'ms', 'Malay', 'Halia', 'Latin', '2026-06-26 15:48:13'),
    (325, 'Zingiber officinale', 'tl', 'Filipino (Tagalog)', 'Luya', 'Latin', '2026-06-26 15:48:13'),
    (326, 'Zingiber officinale', 'sw', 'Swahili', 'Tangawizi', 'Latin', '2026-06-26 15:48:13'),
    (327, 'Zingiber officinale', 'ha', 'Hausa', 'Cita', 'Latin', '2026-06-26 15:48:13'),
    (328, 'Zingiber officinale', 'pt', 'Portuguese', 'Gengibre', 'Latin', '2026-06-26 15:48:13'),
    (329, 'Zingiber officinale', 'es', 'Spanish', 'Jengibre', 'Latin', '2026-06-26 15:48:13'),
    (330, 'Zingiber officinale', 'fr', 'French', 'Gingembre', 'Latin', '2026-06-26 15:48:13'),
    (331, 'Zingiber officinale', 'de', 'German', 'Ingwer', 'Latin', '2026-06-26 15:48:13'),
    (332, 'Zingiber officinale', 'it', 'Italian', 'Zenzero', 'Native', '2026-06-26 15:48:13'),
    (333, 'Zingiber officinale', 'ru', 'Russian', 'Imbir (имбирь)', 'Native', '2026-06-26 15:48:13'),
    (334, 'Zingiber officinale', 'tr', 'Turkish', 'Zencefil', 'Latin', '2026-06-26 15:48:13'),
    (335, 'Curcuma longa', 'en', 'English', 'Turmeric', 'Latin', '2026-06-26 15:48:13'),
    (336, 'Curcuma longa', 'hi', 'Hindi', 'Haldi (हल्दी)', 'Native', '2026-06-26 15:48:13'),
    (337, 'Curcuma longa', 'bn', 'Bengali', 'Halud (হলুদ)', 'Native', '2026-06-26 15:48:13'),
    (338, 'Curcuma longa', 'te', 'Telugu', 'Pasupu (పసుపు)', 'Native', '2026-06-26 15:48:13'),
    (339, 'Curcuma longa', 'ta', 'Tamil', 'Manjal (மஞ்சள்)', 'Native', '2026-06-26 15:48:13'),
    (340, 'Curcuma longa', 'kn', 'Kannada', 'Arisina (ಅರಿಶಿನ)', 'Native', '2026-06-26 15:48:13'),
    (341, 'Curcuma longa', 'ml', 'Malayalam', 'Manjal (മഞ്ഞൾ)', 'Native', '2026-06-26 15:48:13'),
    (342, 'Curcuma longa', 'mr', 'Marathi', 'Halad (हळद)', 'Native', '2026-06-26 15:48:13'),
    (343, 'Curcuma longa', 'pa', 'Punjabi', 'Haldi (ਹਲਦੀ)', 'Native', '2026-06-26 15:48:13'),
    (344, 'Curcuma longa', 'gu', 'Gujarati', 'Haldar (હળદર)', 'Native', '2026-06-26 15:48:13'),
    (345, 'Curcuma longa', 'ur', 'Urdu', 'Haldi (ہلدی)', 'Native', '2026-06-26 15:48:13'),
    (346, 'Curcuma longa', 'ar', 'Arabic', 'Kurkum (كركم)', 'Native', '2026-06-26 15:48:13'),
    (347, 'Curcuma longa', 'zh', 'Chinese (Mandarin)', 'Jiānghuáng (姜黄)', 'Native', '2026-06-26 15:48:13'),
    (348, 'Curcuma longa', 'ja', 'Japanese', 'Ukon (ウコン)', 'Native', '2026-06-26 15:48:13'),
    (349, 'Curcuma longa', 'ko', 'Korean', 'Ulgeumchai (울금)', 'Native', '2026-06-26 15:48:13'),
    (350, 'Curcuma longa', 'vi', 'Vietnamese', 'Nghệ', 'Latin', '2026-06-26 15:48:13'),
    (351, 'Curcuma longa', 'th', 'Thai', 'Kha min (ขมิ้น)', 'Native', '2026-06-26 15:48:13'),
    (352, 'Curcuma longa', 'id', 'Indonesian', 'Kunyit', 'Latin', '2026-06-26 15:48:13'),
    (353, 'Curcuma longa', 'ms', 'Malay', 'Kunyit', 'Latin', '2026-06-26 15:48:13'),
    (354, 'Curcuma longa', 'tl', 'Filipino (Tagalog)', 'Dilaw', 'Latin', '2026-06-26 15:48:13'),
    (355, 'Curcuma longa', 'sw', 'Swahili', 'Manjano', 'Latin', '2026-06-26 15:48:13'),
    (356, 'Curcuma longa', 'ha', 'Hausa', 'Gangamau', 'Latin', '2026-06-26 15:48:13'),
    (357, 'Curcuma longa', 'pt', 'Portuguese', 'Açafrão-da-índia', 'Latin', '2026-06-26 15:48:13'),
    (358, 'Curcuma longa', 'es', 'Spanish', 'Cúrcuma', 'Latin', '2026-06-26 15:48:13'),
    (359, 'Curcuma longa', 'fr', 'French', 'Curcuma', 'Latin', '2026-06-26 15:48:13'),
    (360, 'Curcuma longa', 'de', 'German', 'Kurkuma', 'Latin', '2026-06-26 15:48:13'),
    (361, 'Curcuma longa', 'it', 'Italian', 'Curcuma', 'Native', '2026-06-26 15:48:13'),
    (362, 'Curcuma longa', 'ru', 'Russian', 'Kurkuma (куркума)', 'Native', '2026-06-26 15:48:13'),
    (363, 'Carica papaya', 'en', 'English', 'Papaya', 'Latin', '2026-06-26 15:48:13'),
    (364, 'Carica papaya', 'hi', 'Hindi', 'Papita (पपीता)', 'Native', '2026-06-26 15:48:13'),
    (365, 'Carica papaya', 'bn', 'Bengali', 'Pepe (পেঁপে)', 'Native', '2026-06-26 15:48:13'),
    (366, 'Carica papaya', 'te', 'Telugu', 'Boppai Pandu (బొప్పాయి)', 'Native', '2026-06-26 15:48:13'),
    (367, 'Carica papaya', 'ta', 'Tamil', 'Pappali (பப்பாளி)', 'Native', '2026-06-26 15:48:13'),
    (368, 'Carica papaya', 'kn', 'Kannada', 'Pappayi (ಪಪ್ಪಾಯ)', 'Native', '2026-06-26 15:48:13'),
    (369, 'Carica papaya', 'ml', 'Malayalam', 'Papaya (പപ്പായ)', 'Native', '2026-06-26 15:48:13'),
    (370, 'Carica papaya', 'mr', 'Marathi', 'Papai (पपई)', 'Native', '2026-06-26 15:48:13'),
    (371, 'Carica papaya', 'pa', 'Punjabi', 'Papita (ਪਪੀਤਾ)', 'Native', '2026-06-26 15:48:13'),
    (372, 'Carica papaya', 'gu', 'Gujarati', 'Papaya (પપૈયા)', 'Native', '2026-06-26 15:48:13'),
    (373, 'Carica papaya', 'ur', 'Urdu', 'Papita (پپیتا)', 'Native', '2026-06-26 15:48:13'),
    (374, 'Carica papaya', 'ar', 'Arabic', 'Babaya (بابايا)', 'Native', '2026-06-26 15:48:13'),
    (375, 'Carica papaya', 'zh', 'Chinese (Mandarin)', 'Mùguā (木瓜)', 'Native', '2026-06-26 15:48:13'),
    (376, 'Carica papaya', 'ja', 'Japanese', 'Papaya (パパイア)', 'Native', '2026-06-26 15:48:13'),
    (377, 'Carica papaya', 'ko', 'Korean', 'Papaya (파파야)', 'Native', '2026-06-26 15:48:13'),
    (378, 'Carica papaya', 'vi', 'Vietnamese', 'Đu đủ', 'Latin', '2026-06-26 15:48:13'),
    (379, 'Carica papaya', 'th', 'Thai', 'Malako (มะละกอ)', 'Native', '2026-06-26 15:48:13'),
    (380, 'Carica papaya', 'id', 'Indonesian', 'Pepaya', 'Latin', '2026-06-26 15:48:13'),
    (381, 'Carica papaya', 'ms', 'Malay', 'Betik', 'Latin', '2026-06-26 15:48:13'),
    (382, 'Carica papaya', 'tl', 'Filipino (Tagalog)', 'Papaya', 'Latin', '2026-06-26 15:48:13'),
    (383, 'Carica papaya', 'sw', 'Swahili', 'Papai', 'Latin', '2026-06-26 15:48:13'),
    (384, 'Carica papaya', 'ha', 'Hausa', 'Gwandaflawa', 'Latin', '2026-06-26 15:48:13'),
    (385, 'Carica papaya', 'yo', 'Yoruba', 'Ìbépé', 'Latin', '2026-06-26 15:48:13'),
    (386, 'Carica papaya', 'pt', 'Portuguese', 'Mamão', 'Latin', '2026-06-26 15:48:13'),
    (387, 'Carica papaya', 'es', 'Spanish', 'Papaya', 'Latin', '2026-06-26 15:48:13'),
    (388, 'Carica papaya', 'fr', 'French', 'Papaye', 'Latin', '2026-06-26 15:48:13'),
    (389, 'Carica papaya', 'de', 'German', 'Papaya', 'Latin', '2026-06-26 15:48:13'),
    (390, 'Carica papaya', 'it', 'Italian', 'Papaia', 'Native', '2026-06-26 15:48:13'),
    (391, 'Carica papaya', 'ru', 'Russian', 'Papaya (папайя)', 'Native', '2026-06-26 15:48:13'),
    (392, 'Glycine max', 'en', 'English', 'Soybean', 'Latin', '2026-06-26 15:48:13'),
    (393, 'Glycine max', 'hi', 'Hindi', 'Soyabean (सोयाबीन)', 'Native', '2026-06-26 15:48:13'),
    (394, 'Glycine max', 'bn', 'Bengali', 'Soya (সয়া)', 'Native', '2026-06-26 15:48:13'),
    (395, 'Glycine max', 'te', 'Telugu', 'Soya Ginjalu (సోయా)', 'Native', '2026-06-26 15:48:13'),
    (396, 'Glycine max', 'ta', 'Tamil', 'Soya (சோயா)', 'Native', '2026-06-26 15:48:13'),
    (397, 'Glycine max', 'kn', 'Kannada', 'Soya (ಸೋಯಾ)', 'Native', '2026-06-26 15:48:13'),
    (398, 'Glycine max', 'ml', 'Malayalam', 'Soya Bean (സോയ ബീൻ)', 'Native', '2026-06-26 15:48:13'),
    (399, 'Glycine max', 'mr', 'Marathi', 'Soybean (सोयाबीन)', 'Native', '2026-06-26 15:48:13'),
    (400, 'Glycine max', 'ur', 'Urdu', 'Soya (سویا)', 'Native', '2026-06-26 15:48:13');
INSERT INTO multilingual_names (id, botanical_name, language_code, language_name, local_name, script, created_at) VALUES
    (401, 'Glycine max', 'ar', 'Arabic', 'Soya (فول الصويا)', 'Native', '2026-06-26 15:48:13'),
    (402, 'Glycine max', 'zh', 'Chinese (Mandarin)', 'Dàdòu (大豆)', 'Native', '2026-06-26 15:48:13'),
    (403, 'Glycine max', 'ja', 'Japanese', 'Daizu (大豆)', 'Native', '2026-06-26 15:48:13'),
    (404, 'Glycine max', 'ko', 'Korean', 'Kong (콩)', 'Native', '2026-06-26 15:48:13'),
    (405, 'Glycine max', 'vi', 'Vietnamese', 'Đậu nành', 'Latin', '2026-06-26 15:48:13'),
    (406, 'Glycine max', 'th', 'Thai', 'Thua Lueang (ถั่วเหลือง)', 'Native', '2026-06-26 15:48:13'),
    (407, 'Glycine max', 'id', 'Indonesian', 'Kedelai', 'Latin', '2026-06-26 15:48:13'),
    (408, 'Glycine max', 'ms', 'Malay', 'Kacang soya', 'Latin', '2026-06-26 15:48:13'),
    (409, 'Glycine max', 'tl', 'Filipino (Tagalog)', 'Soybean', 'Latin', '2026-06-26 15:48:13'),
    (410, 'Glycine max', 'sw', 'Swahili', 'Soya', 'Latin', '2026-06-26 15:48:13'),
    (411, 'Glycine max', 'pt', 'Portuguese', 'Soja', 'Latin', '2026-06-26 15:48:13'),
    (412, 'Glycine max', 'es', 'Spanish', 'Soja', 'Latin', '2026-06-26 15:48:13'),
    (413, 'Glycine max', 'fr', 'French', 'Soja', 'Latin', '2026-06-26 15:48:13'),
    (414, 'Glycine max', 'de', 'German', 'Sojabohne', 'Latin', '2026-06-26 15:48:13'),
    (415, 'Glycine max', 'it', 'Italian', 'Soia', 'Native', '2026-06-26 15:48:13'),
    (416, 'Glycine max', 'ru', 'Russian', 'Soya (соя)', 'Native', '2026-06-26 15:48:13'),
    (417, 'Glycine max', 'tr', 'Turkish', 'Soya fasulyesi', 'Latin', '2026-06-26 15:48:13'),
    (418, 'Cicer arietinum', 'en', 'English', 'Chickpea (Bengal Gram)', 'Latin', '2026-06-26 15:48:13'),
    (419, 'Cicer arietinum', 'hi', 'Hindi', 'Chana (चना)', 'Native', '2026-06-26 15:48:13'),
    (420, 'Cicer arietinum', 'bn', 'Bengali', 'Boot (বুট)', 'Native', '2026-06-26 15:48:13'),
    (421, 'Cicer arietinum', 'te', 'Telugu', 'Sanagalu (సెనగలు)', 'Native', '2026-06-26 15:48:13'),
    (422, 'Cicer arietinum', 'ta', 'Tamil', 'Kadalai (கடலை)', 'Native', '2026-06-26 15:48:13'),
    (423, 'Cicer arietinum', 'kn', 'Kannada', 'Kadale (ಕಡಲೆ)', 'Native', '2026-06-26 15:48:13'),
    (424, 'Cicer arietinum', 'ml', 'Malayalam', 'Kadala (കടല)', 'Native', '2026-06-26 15:48:13'),
    (425, 'Cicer arietinum', 'mr', 'Marathi', 'Harbhara (हरभरा)', 'Native', '2026-06-26 15:48:13'),
    (426, 'Cicer arietinum', 'pa', 'Punjabi', 'Chhole (ਛੋਲੇ)', 'Native', '2026-06-26 15:48:13'),
    (427, 'Cicer arietinum', 'gu', 'Gujarati', 'Chana (ચણા)', 'Native', '2026-06-26 15:48:13'),
    (428, 'Cicer arietinum', 'ur', 'Urdu', 'Chana (چنا)', 'Native', '2026-06-26 15:48:13'),
    (429, 'Cicer arietinum', 'ar', 'Arabic', 'Hummus (حمص)', 'Native', '2026-06-26 15:48:13'),
    (430, 'Cicer arietinum', 'zh', 'Chinese (Mandarin)', 'Ying zuì dòu (鹰嘴豆)', 'Native', '2026-06-26 15:48:13'),
    (431, 'Cicer arietinum', 'ja', 'Japanese', 'Hiyo kobe (ひよこ豆)', 'Native', '2026-06-26 15:48:13'),
    (432, 'Cicer arietinum', 'ko', 'Korean', 'Chickpea (병아리콩)', 'Native', '2026-06-26 15:48:13'),
    (433, 'Cicer arietinum', 'vi', 'Vietnamese', 'Đậu gà', 'Latin', '2026-06-26 15:48:13'),
    (434, 'Cicer arietinum', 'th', 'Thai', 'Thua kho (ถั่วลูกไก่)', 'Native', '2026-06-26 15:48:13'),
    (435, 'Cicer arietinum', 'id', 'Indonesian', 'Kacang Arab', 'Latin', '2026-06-26 15:48:13'),
    (436, 'Cicer arietinum', 'ms', 'Malay', 'Kacang kuda', 'Latin', '2026-06-26 15:48:13'),
    (437, 'Cicer arietinum', 'tl', 'Filipino (Tagalog)', 'Garbanzos', 'Latin', '2026-06-26 15:48:13'),
    (438, 'Cicer arietinum', 'sw', 'Swahili', 'Njegere', 'Latin', '2026-06-26 15:48:13'),
    (439, 'Cicer arietinum', 'ha', 'Hausa', 'Agwado', 'Latin', '2026-06-26 15:48:13'),
    (440, 'Cicer arietinum', 'pt', 'Portuguese', 'Grão-de-bico', 'Latin', '2026-06-26 15:48:13'),
    (441, 'Cicer arietinum', 'es', 'Spanish', 'Garbanzo', 'Latin', '2026-06-26 15:48:13'),
    (442, 'Cicer arietinum', 'fr', 'French', 'Pois chiche', 'Latin', '2026-06-26 15:48:13'),
    (443, 'Cicer arietinum', 'de', 'German', 'Kichererbse', 'Latin', '2026-06-26 15:48:13'),
    (444, 'Cicer arietinum', 'it', 'Italian', 'Cece', 'Native', '2026-06-26 15:48:13'),
    (445, 'Cicer arietinum', 'ru', 'Russian', 'Nut (нут)', 'Native', '2026-06-26 15:48:13'),
    (446, 'Cicer arietinum', 'tr', 'Turkish', 'Nohut', 'Latin', '2026-06-26 15:48:13'),
    (447, 'Cajanus cajan', 'en', 'English', 'Pigeon Pea (Red Gram)', 'Latin', '2026-06-26 15:48:13'),
    (448, 'Cajanus cajan', 'hi', 'Hindi', 'Arhar / Tur (अरहर)', 'Native', '2026-06-26 15:48:13'),
    (449, 'Cajanus cajan', 'bn', 'Bengali', 'Arhar (অড়হর)', 'Native', '2026-06-26 15:48:13'),
    (450, 'Cajanus cajan', 'te', 'Telugu', 'Kandi Pappu (కంది పప్పు)', 'Native', '2026-06-26 15:48:13'),
    (451, 'Cajanus cajan', 'ta', 'Tamil', 'Thuvaram (துவரை)', 'Native', '2026-06-26 15:48:13'),
    (452, 'Cajanus cajan', 'kn', 'Kannada', 'Thogari (ತೊಗರಿ)', 'Native', '2026-06-26 15:48:13'),
    (453, 'Cajanus cajan', 'ml', 'Malayalam', 'Thuvara (തുവര)', 'Native', '2026-06-26 15:48:13'),
    (454, 'Cajanus cajan', 'mr', 'Marathi', 'Tur (तूर)', 'Native', '2026-06-26 15:48:13'),
    (455, 'Cajanus cajan', 'pa', 'Punjabi', 'Arhar (ਅਰਹਰ)', 'Native', '2026-06-26 15:48:13'),
    (456, 'Cajanus cajan', 'gu', 'Gujarati', 'Tuver (તુવેર)', 'Native', '2026-06-26 15:48:13'),
    (457, 'Cajanus cajan', 'ur', 'Urdu', 'Arhar (ارہر)', 'Native', '2026-06-26 15:48:13'),
    (458, 'Cajanus cajan', 'ar', 'Arabic', 'Adas (عدس حلبي)', 'Native', '2026-06-26 15:48:13'),
    (459, 'Cajanus cajan', 'sw', 'Swahili', 'Mbaazi', 'Latin', '2026-06-26 15:48:13'),
    (460, 'Cajanus cajan', 'ha', 'Hausa', 'Wake', 'Latin', '2026-06-26 15:48:13'),
    (461, 'Cajanus cajan', 'yo', 'Yoruba', 'Ẹ̀wà', 'Latin', '2026-06-26 15:48:13'),
    (462, 'Cajanus cajan', 'pt', 'Portuguese', 'Ervilha-pombo', 'Latin', '2026-06-26 15:48:13'),
    (463, 'Cajanus cajan', 'es', 'Spanish', 'Gandul', 'Latin', '2026-06-26 15:48:13'),
    (464, 'Cajanus cajan', 'fr', 'French', 'Pois d''Angole', 'Latin', '2026-06-26 15:48:13'),
    (465, 'Cajanus cajan', 'de', 'German', 'Straucherbse', 'Latin', '2026-06-26 15:48:13'),
    (466, 'Vigna radiata', 'en', 'English', 'Mung Bean (Green Gram)', 'Latin', '2026-06-26 15:48:13'),
    (467, 'Vigna radiata', 'hi', 'Hindi', 'Moong (मूंग)', 'Native', '2026-06-26 15:48:13'),
    (468, 'Vigna radiata', 'bn', 'Bengali', 'Mug (মুগ)', 'Native', '2026-06-26 15:48:13'),
    (469, 'Vigna radiata', 'te', 'Telugu', 'Pesalu (పెసలు)', 'Native', '2026-06-26 15:48:13'),
    (470, 'Vigna radiata', 'ta', 'Tamil', 'Pasiparuppu (பாசிப்பருப்பு)', 'Native', '2026-06-26 15:48:13'),
    (471, 'Vigna radiata', 'kn', 'Kannada', 'Hesaru Kaalu (ಹೆಸರು ಕಾಳು)', 'Native', '2026-06-26 15:48:13'),
    (472, 'Vigna radiata', 'ml', 'Malayalam', 'Cherupayar (ചെറുപയർ)', 'Native', '2026-06-26 15:48:13'),
    (473, 'Vigna radiata', 'mr', 'Marathi', 'Mug (मूग)', 'Native', '2026-06-26 15:48:13'),
    (474, 'Vigna radiata', 'pa', 'Punjabi', 'Mung (ਮੂੰਗ)', 'Native', '2026-06-26 15:48:13'),
    (475, 'Vigna radiata', 'gu', 'Gujarati', 'Moong (મગ)', 'Native', '2026-06-26 15:48:13'),
    (476, 'Vigna radiata', 'ur', 'Urdu', 'Moong (مونگ)', 'Native', '2026-06-26 15:48:13'),
    (477, 'Vigna radiata', 'ar', 'Arabic', 'Adas Akhdar (عدس أخضر)', 'Native', '2026-06-26 15:48:13'),
    (478, 'Vigna radiata', 'zh', 'Chinese (Mandarin)', 'Lǜdòu (绿豆)', 'Native', '2026-06-26 15:48:13'),
    (479, 'Vigna radiata', 'ja', 'Japanese', 'Ryokuto (緑豆)', 'Native', '2026-06-26 15:48:13'),
    (480, 'Vigna radiata', 'ko', 'Korean', 'Nokdu (녹두)', 'Native', '2026-06-26 15:48:13'),
    (481, 'Vigna radiata', 'vi', 'Vietnamese', 'Đậu xanh', 'Latin', '2026-06-26 15:48:13'),
    (482, 'Vigna radiata', 'th', 'Thai', 'Thua khiao (ถั่วเขียว)', 'Native', '2026-06-26 15:48:13'),
    (483, 'Vigna radiata', 'id', 'Indonesian', 'Kacang hijau', 'Latin', '2026-06-26 15:48:13'),
    (484, 'Vigna radiata', 'ms', 'Malay', 'Kacang hijau', 'Latin', '2026-06-26 15:48:13'),
    (485, 'Vigna radiata', 'tl', 'Filipino (Tagalog)', 'Munggo', 'Latin', '2026-06-26 15:48:13'),
    (486, 'Vigna radiata', 'sw', 'Swahili', 'Maharagwe ya kijani', 'Latin', '2026-06-26 15:48:13'),
    (487, 'Vigna radiata', 'pt', 'Portuguese', 'Feijão-verde', 'Latin', '2026-06-26 15:48:13'),
    (488, 'Vigna radiata', 'es', 'Spanish', 'Frijol mungo', 'Latin', '2026-06-26 15:48:13'),
    (489, 'Vigna radiata', 'fr', 'French', 'Haricot mungo', 'Latin', '2026-06-26 15:48:13'),
    (490, 'Vigna radiata', 'de', 'German', 'Mungbohne', 'Latin', '2026-06-26 15:48:13'),
    (491, 'Arachis hypogaea', 'en', 'English', 'Groundnut / Peanut', 'Latin', '2026-06-26 15:48:13'),
    (492, 'Arachis hypogaea', 'hi', 'Hindi', 'Mungphali (मूंगफली)', 'Native', '2026-06-26 15:48:13'),
    (493, 'Arachis hypogaea', 'bn', 'Bengali', 'Cheenabadam (চিনাবাদাম)', 'Native', '2026-06-26 15:48:13'),
    (494, 'Arachis hypogaea', 'te', 'Telugu', 'Verusenaga (వేరుసెనగ)', 'Native', '2026-06-26 15:48:13'),
    (495, 'Arachis hypogaea', 'ta', 'Tamil', 'Kadalai (கடலை)', 'Native', '2026-06-26 15:48:13'),
    (496, 'Arachis hypogaea', 'kn', 'Kannada', 'Kadalekayi (ಕಡ್ಲೇಕಾಯಿ)', 'Native', '2026-06-26 15:48:13'),
    (497, 'Arachis hypogaea', 'ml', 'Malayalam', 'Nelakadala (നിലക്കടല)', 'Native', '2026-06-26 15:48:13'),
    (498, 'Arachis hypogaea', 'mr', 'Marathi', 'Shengan (शेंगाना)', 'Native', '2026-06-26 15:48:13'),
    (499, 'Arachis hypogaea', 'pa', 'Punjabi', 'Moonphali (ਮੂੰਗਫਲੀ)', 'Native', '2026-06-26 15:48:13'),
    (500, 'Arachis hypogaea', 'gu', 'Gujarati', 'Shing (સિંગ)', 'Native', '2026-06-26 15:48:13');
INSERT INTO multilingual_names (id, botanical_name, language_code, language_name, local_name, script, created_at) VALUES
    (501, 'Arachis hypogaea', 'ur', 'Urdu', 'Moonphali (مونگ پھلی)', 'Native', '2026-06-26 15:48:13'),
    (502, 'Arachis hypogaea', 'ar', 'Arabic', 'Ful Sudan (فول سوداني)', 'Native', '2026-06-26 15:48:13'),
    (503, 'Arachis hypogaea', 'zh', 'Chinese (Mandarin)', 'Huāshēng (花生)', 'Native', '2026-06-26 15:48:13'),
    (504, 'Arachis hypogaea', 'ja', 'Japanese', 'Rakkasei (落花生)', 'Native', '2026-06-26 15:48:13'),
    (505, 'Arachis hypogaea', 'ko', 'Korean', 'Ttangkong (땅콩)', 'Native', '2026-06-26 15:48:13'),
    (506, 'Arachis hypogaea', 'vi', 'Vietnamese', 'Lạc / Đậu phộng', 'Latin', '2026-06-26 15:48:13'),
    (507, 'Arachis hypogaea', 'th', 'Thai', 'Thua lisong (ถั่วลิสง)', 'Native', '2026-06-26 15:48:13'),
    (508, 'Arachis hypogaea', 'id', 'Indonesian', 'Kacang tanah', 'Latin', '2026-06-26 15:48:13'),
    (509, 'Arachis hypogaea', 'ms', 'Malay', 'Kacang tanah', 'Latin', '2026-06-26 15:48:13'),
    (510, 'Arachis hypogaea', 'tl', 'Filipino (Tagalog)', 'Mani', 'Latin', '2026-06-26 15:48:13'),
    (511, 'Arachis hypogaea', 'sw', 'Swahili', 'Karanga', 'Latin', '2026-06-26 15:48:13'),
    (512, 'Arachis hypogaea', 'ha', 'Hausa', 'Gyada', 'Latin', '2026-06-26 15:48:13'),
    (513, 'Arachis hypogaea', 'yo', 'Yoruba', 'Epa', 'Latin', '2026-06-26 15:48:13'),
    (514, 'Arachis hypogaea', 'ig', 'Igbo', 'Ahụ̀ọ̀cha', 'Native', '2026-06-26 15:48:13'),
    (515, 'Arachis hypogaea', 'am', 'Amharic', 'Yegena ater (የጤፍ)', 'Native', '2026-06-26 15:48:13'),
    (516, 'Arachis hypogaea', 'pt', 'Portuguese', 'Amendoim', 'Latin', '2026-06-26 15:48:13'),
    (517, 'Arachis hypogaea', 'es', 'Spanish', 'Cacahuate/Maní', 'Latin', '2026-06-26 15:48:13'),
    (518, 'Arachis hypogaea', 'fr', 'French', 'Arachide', 'Latin', '2026-06-26 15:48:13'),
    (519, 'Arachis hypogaea', 'de', 'German', 'Erdnuss', 'Latin', '2026-06-26 15:48:13'),
    (520, 'Arachis hypogaea', 'it', 'Italian', 'Arachide', 'Native', '2026-06-26 15:48:13'),
    (521, 'Arachis hypogaea', 'ru', 'Russian', 'Arakhis (арахис)', 'Native', '2026-06-26 15:48:13'),
    (522, 'Arachis hypogaea', 'tr', 'Turkish', 'Yerfıstığı', 'Latin', '2026-06-26 15:48:13'),
    (523, 'Cocos nucifera', 'en', 'English', 'Coconut', 'Latin', '2026-06-26 15:48:13'),
    (524, 'Cocos nucifera', 'hi', 'Hindi', 'Nariyal (नारियल)', 'Native', '2026-06-26 15:48:13'),
    (525, 'Cocos nucifera', 'bn', 'Bengali', 'Narkel (নারকেল)', 'Native', '2026-06-26 15:48:13'),
    (526, 'Cocos nucifera', 'te', 'Telugu', 'Kobbari (కొబ్బరి)', 'Native', '2026-06-26 15:48:13'),
    (527, 'Cocos nucifera', 'ta', 'Tamil', 'Thengai (தேங்காய்)', 'Native', '2026-06-26 15:48:13'),
    (528, 'Cocos nucifera', 'kn', 'Kannada', 'Tenginakayi (ತೆಂಗಿನಕಾಯಿ)', 'Native', '2026-06-26 15:48:13'),
    (529, 'Cocos nucifera', 'ml', 'Malayalam', 'Thenga (തെങ്ങ്)', 'Native', '2026-06-26 15:48:13'),
    (530, 'Cocos nucifera', 'mr', 'Marathi', 'Naral (नारळ)', 'Native', '2026-06-26 15:48:13'),
    (531, 'Cocos nucifera', 'pa', 'Punjabi', 'Nariyal (ਨਾਰੀਅਲ)', 'Native', '2026-06-26 15:48:13'),
    (532, 'Cocos nucifera', 'gu', 'Gujarati', 'Nadiyer (નારિયેળ)', 'Native', '2026-06-26 15:48:13'),
    (533, 'Cocos nucifera', 'ur', 'Urdu', 'Nariyal (ناریل)', 'Native', '2026-06-26 15:48:13'),
    (534, 'Cocos nucifera', 'ar', 'Arabic', 'Jawz al-hind (جوز الهند)', 'Native', '2026-06-26 15:48:13'),
    (535, 'Cocos nucifera', 'zh', 'Chinese (Mandarin)', 'Yēzi (椰子)', 'Native', '2026-06-26 15:48:13'),
    (536, 'Cocos nucifera', 'ja', 'Japanese', 'Kokonattsu (ヤシの実)', 'Native', '2026-06-26 15:48:13'),
    (537, 'Cocos nucifera', 'ko', 'Korean', 'Coconut (코코넛)', 'Native', '2026-06-26 15:48:13'),
    (538, 'Cocos nucifera', 'vi', 'Vietnamese', 'Dừa', 'Latin', '2026-06-26 15:48:13'),
    (539, 'Cocos nucifera', 'th', 'Thai', 'Maphrao (มะพร้าว)', 'Native', '2026-06-26 15:48:13'),
    (540, 'Cocos nucifera', 'id', 'Indonesian', 'Kelapa', 'Latin', '2026-06-26 15:48:13'),
    (541, 'Cocos nucifera', 'ms', 'Malay', 'Kelapa', 'Latin', '2026-06-26 15:48:13'),
    (542, 'Cocos nucifera', 'tl', 'Filipino (Tagalog)', 'Niyog', 'Latin', '2026-06-26 15:48:13'),
    (543, 'Cocos nucifera', 'sw', 'Swahili', 'Nazi', 'Latin', '2026-06-26 15:48:13'),
    (544, 'Cocos nucifera', 'ha', 'Hausa', 'Kwakwa', 'Latin', '2026-06-26 15:48:13'),
    (545, 'Cocos nucifera', 'yo', 'Yoruba', 'Agbon', 'Latin', '2026-06-26 15:48:13'),
    (546, 'Cocos nucifera', 'pt', 'Portuguese', 'Coco', 'Latin', '2026-06-26 15:48:13'),
    (547, 'Cocos nucifera', 'es', 'Spanish', 'Coco', 'Latin', '2026-06-26 15:48:13'),
    (548, 'Cocos nucifera', 'fr', 'French', 'Noix de coco', 'Latin', '2026-06-26 15:48:13'),
    (549, 'Cocos nucifera', 'de', 'German', 'Kokosnuss', 'Latin', '2026-06-26 15:48:13'),
    (550, 'Cocos nucifera', 'it', 'Italian', 'Noce di cocco', 'Native', '2026-06-26 15:48:13'),
    (551, 'Cocos nucifera', 'ru', 'Russian', 'Kokos (кокос)', 'Native', '2026-06-26 15:48:13'),
    (552, 'Saccharum officinarum', 'en', 'English', 'Sugarcane', 'Latin', '2026-06-26 15:48:13'),
    (553, 'Saccharum officinarum', 'hi', 'Hindi', 'Ganna (गन्ना)', 'Native', '2026-06-26 15:48:13'),
    (554, 'Saccharum officinarum', 'bn', 'Bengali', 'Aakh (আখ)', 'Native', '2026-06-26 15:48:13'),
    (555, 'Saccharum officinarum', 'te', 'Telugu', 'Cheruku (చెరుకు)', 'Native', '2026-06-26 15:48:13'),
    (556, 'Saccharum officinarum', 'ta', 'Tamil', 'Karumbu (கரும்பு)', 'Native', '2026-06-26 15:48:13'),
    (557, 'Saccharum officinarum', 'kn', 'Kannada', 'Kabbu (ಕಬ್ಬು)', 'Native', '2026-06-26 15:48:13'),
    (558, 'Saccharum officinarum', 'ml', 'Malayalam', 'Karumbu (കരിമ്പ്)', 'Native', '2026-06-26 15:48:13'),
    (559, 'Saccharum officinarum', 'mr', 'Marathi', 'Oos (ऊस)', 'Native', '2026-06-26 15:48:13'),
    (560, 'Saccharum officinarum', 'pa', 'Punjabi', 'Ganna (ਗੰਨਾ)', 'Native', '2026-06-26 15:48:13'),
    (561, 'Saccharum officinarum', 'gu', 'Gujarati', 'Svaradi (શેરડી)', 'Native', '2026-06-26 15:48:13'),
    (562, 'Saccharum officinarum', 'ur', 'Urdu', 'Ganna (گنا)', 'Native', '2026-06-26 15:48:13'),
    (563, 'Saccharum officinarum', 'ar', 'Arabic', 'Qasab al-sukkar (قصب السكر)', 'Native', '2026-06-26 15:48:13'),
    (564, 'Saccharum officinarum', 'zh', 'Chinese (Mandarin)', 'Gānzhè (甘蔗)', 'Native', '2026-06-26 15:48:13'),
    (565, 'Saccharum officinarum', 'ja', 'Japanese', 'Satōkibi (サトウキビ)', 'Native', '2026-06-26 15:48:13'),
    (566, 'Saccharum officinarum', 'ko', 'Korean', 'Satong Susu (사탕수수)', 'Native', '2026-06-26 15:48:13'),
    (567, 'Saccharum officinarum', 'vi', 'Vietnamese', 'Mía', 'Latin', '2026-06-26 15:48:13'),
    (568, 'Saccharum officinarum', 'th', 'Thai', 'Oi (อ้อย)', 'Native', '2026-06-26 15:48:13'),
    (569, 'Saccharum officinarum', 'id', 'Indonesian', 'Tebu', 'Latin', '2026-06-26 15:48:13'),
    (570, 'Saccharum officinarum', 'ms', 'Malay', 'Tebu', 'Latin', '2026-06-26 15:48:13'),
    (571, 'Saccharum officinarum', 'tl', 'Filipino (Tagalog)', 'Tubo', 'Latin', '2026-06-26 15:48:13'),
    (572, 'Saccharum officinarum', 'sw', 'Swahili', 'Miwa', 'Latin', '2026-06-26 15:48:13'),
    (573, 'Saccharum officinarum', 'ha', 'Hausa', 'Rake', 'Latin', '2026-06-26 15:48:13'),
    (574, 'Saccharum officinarum', 'yo', 'Yoruba', 'Ireke', 'Latin', '2026-06-26 15:48:13'),
    (575, 'Saccharum officinarum', 'pt', 'Portuguese', 'Cana-de-açúcar', 'Latin', '2026-06-26 15:48:13'),
    (576, 'Saccharum officinarum', 'es', 'Spanish', 'Caña de azúcar', 'Latin', '2026-06-26 15:48:13'),
    (577, 'Saccharum officinarum', 'fr', 'French', 'Canne à sucre', 'Latin', '2026-06-26 15:48:13'),
    (578, 'Saccharum officinarum', 'de', 'German', 'Zuckerrohr', 'Latin', '2026-06-26 15:48:13'),
    (579, 'Saccharum officinarum', 'it', 'Italian', 'Canna da zucchero', 'Native', '2026-06-26 15:48:13'),
    (580, 'Saccharum officinarum', 'ru', 'Russian', 'Sakharniy trostnik (сахарный тростник)', 'Native', '2026-06-26 15:48:13'),
    (581, 'Gossypium hirsutum', 'en', 'English', 'Cotton', 'Latin', '2026-06-26 15:48:13'),
    (582, 'Gossypium hirsutum', 'hi', 'Hindi', 'Kapas (कपास)', 'Native', '2026-06-26 15:48:13'),
    (583, 'Gossypium hirsutum', 'bn', 'Bengali', 'Kapas (কাপাস)', 'Native', '2026-06-26 15:48:13'),
    (584, 'Gossypium hirsutum', 'te', 'Telugu', 'Patti (పత్తి)', 'Native', '2026-06-26 15:48:13'),
    (585, 'Gossypium hirsutum', 'ta', 'Tamil', 'Panjhu (பஞ்சு)', 'Native', '2026-06-26 15:48:13'),
    (586, 'Gossypium hirsutum', 'kn', 'Kannada', 'Hatti (ಹತ್ತಿ)', 'Native', '2026-06-26 15:48:13'),
    (587, 'Gossypium hirsutum', 'ml', 'Malayalam', 'Panjhu (പഞ്ഞി)', 'Native', '2026-06-26 15:48:13'),
    (588, 'Gossypium hirsutum', 'mr', 'Marathi', 'Kapus (कापूस)', 'Native', '2026-06-26 15:48:13'),
    (589, 'Gossypium hirsutum', 'pa', 'Punjabi', 'Narma (ਨਰਮਾ)', 'Native', '2026-06-26 15:48:13'),
    (590, 'Gossypium hirsutum', 'gu', 'Gujarati', 'Kapas (કપાસ)', 'Native', '2026-06-26 15:48:13'),
    (591, 'Gossypium hirsutum', 'ur', 'Urdu', 'Kapas (کپاس)', 'Native', '2026-06-26 15:48:13'),
    (592, 'Gossypium hirsutum', 'ar', 'Arabic', 'Qutn (قطن)', 'Native', '2026-06-26 15:48:13'),
    (593, 'Gossypium hirsutum', 'zh', 'Chinese (Mandarin)', 'Miánhuā (棉花)', 'Native', '2026-06-26 15:48:13'),
    (594, 'Gossypium hirsutum', 'ja', 'Japanese', 'Wata (綿)', 'Native', '2026-06-26 15:48:13'),
    (595, 'Gossypium hirsutum', 'ko', 'Korean', 'Soru (솜)', 'Native', '2026-06-26 15:48:13'),
    (596, 'Gossypium hirsutum', 'vi', 'Vietnamese', 'Bông vải', 'Latin', '2026-06-26 15:48:13'),
    (597, 'Gossypium hirsutum', 'th', 'Thai', 'Fai (ฝ้าย)', 'Native', '2026-06-26 15:48:13'),
    (598, 'Gossypium hirsutum', 'id', 'Indonesian', 'Kapas', 'Latin', '2026-06-26 15:48:13'),
    (599, 'Gossypium hirsutum', 'ms', 'Malay', 'Kapas', 'Latin', '2026-06-26 15:48:13'),
    (600, 'Gossypium hirsutum', 'tl', 'Filipino (Tagalog)', 'Bulak', 'Latin', '2026-06-26 15:48:13');
INSERT INTO multilingual_names (id, botanical_name, language_code, language_name, local_name, script, created_at) VALUES
    (601, 'Gossypium hirsutum', 'sw', 'Swahili', 'Pamba', 'Latin', '2026-06-26 15:48:13'),
    (602, 'Gossypium hirsutum', 'ha', 'Hausa', 'Auduga', 'Latin', '2026-06-26 15:48:13'),
    (603, 'Gossypium hirsutum', 'yo', 'Yoruba', 'Owu', 'Latin', '2026-06-26 15:48:13'),
    (604, 'Gossypium hirsutum', 'pt', 'Portuguese', 'Algodão', 'Latin', '2026-06-26 15:48:13'),
    (605, 'Gossypium hirsutum', 'es', 'Spanish', 'Algodón', 'Latin', '2026-06-26 15:48:13'),
    (606, 'Gossypium hirsutum', 'fr', 'French', 'Coton', 'Latin', '2026-06-26 15:48:13'),
    (607, 'Gossypium hirsutum', 'de', 'German', 'Baumwolle', 'Latin', '2026-06-26 15:48:13'),
    (608, 'Gossypium hirsutum', 'it', 'Italian', 'Cotone', 'Native', '2026-06-26 15:48:13'),
    (609, 'Gossypium hirsutum', 'ru', 'Russian', 'Khlopok (хлопок)', 'Native', '2026-06-26 15:48:13'),
    (610, 'Gossypium hirsutum', 'tr', 'Turkish', 'Pamuk', 'Latin', '2026-06-26 15:48:13'),
    (611, 'Coffea arabica', 'en', 'English', 'Coffee (Arabica)', 'Latin', '2026-06-26 15:48:13'),
    (612, 'Coffea arabica', 'hi', 'Hindi', 'Kahwa (काफी)', 'Native', '2026-06-26 15:48:13'),
    (613, 'Coffea arabica', 'bn', 'Bengali', 'Kafi (কফি)', 'Native', '2026-06-26 15:48:13'),
    (614, 'Coffea arabica', 'te', 'Telugu', 'Coffee (కాఫీ)', 'Native', '2026-06-26 15:48:13'),
    (615, 'Coffea arabica', 'ta', 'Tamil', 'Coffee (காபி)', 'Native', '2026-06-26 15:48:13'),
    (616, 'Coffea arabica', 'kn', 'Kannada', 'Coffee (ಕಾಫಿ)', 'Native', '2026-06-26 15:48:13'),
    (617, 'Coffea arabica', 'ml', 'Malayalam', 'Coffee (കോഫി)', 'Native', '2026-06-26 15:48:13'),
    (618, 'Coffea arabica', 'mr', 'Marathi', 'Coffee (कॉफी)', 'Native', '2026-06-26 15:48:13'),
    (619, 'Coffea arabica', 'ar', 'Arabic', 'Qahwa (قهوة)', 'Native', '2026-06-26 15:48:13'),
    (620, 'Coffea arabica', 'zh', 'Chinese (Mandarin)', 'Kāfēi (咖啡)', 'Native', '2026-06-26 15:48:13'),
    (621, 'Coffea arabica', 'ja', 'Japanese', 'Kōhī (コーヒー)', 'Native', '2026-06-26 15:48:13'),
    (622, 'Coffea arabica', 'ko', 'Korean', 'Keopi (커피)', 'Native', '2026-06-26 15:48:13'),
    (623, 'Coffea arabica', 'vi', 'Vietnamese', 'Cà phê', 'Latin', '2026-06-26 15:48:13'),
    (624, 'Coffea arabica', 'th', 'Thai', 'Kafae (กาแฟ)', 'Native', '2026-06-26 15:48:13'),
    (625, 'Coffea arabica', 'id', 'Indonesian', 'Kopi', 'Latin', '2026-06-26 15:48:13'),
    (626, 'Coffea arabica', 'ms', 'Malay', 'Kopi', 'Latin', '2026-06-26 15:48:13'),
    (627, 'Coffea arabica', 'tl', 'Filipino (Tagalog)', 'Kape', 'Latin', '2026-06-26 15:48:13'),
    (628, 'Coffea arabica', 'sw', 'Swahili', 'Kahawa', 'Latin', '2026-06-26 15:48:13'),
    (629, 'Coffea arabica', 'ha', 'Hausa', 'Kofi', 'Latin', '2026-06-26 15:48:13'),
    (630, 'Coffea arabica', 'yo', 'Yoruba', 'Kòfí', 'Latin', '2026-06-26 15:48:13'),
    (631, 'Coffea arabica', 'am', 'Amharic', 'Bunna (ቡና)', 'Native', '2026-06-26 15:48:13'),
    (632, 'Coffea arabica', 'pt', 'Portuguese', 'Café', 'Latin', '2026-06-26 15:48:13'),
    (633, 'Coffea arabica', 'es', 'Spanish', 'Café', 'Latin', '2026-06-26 15:48:13'),
    (634, 'Coffea arabica', 'fr', 'French', 'Café', 'Latin', '2026-06-26 15:48:13'),
    (635, 'Coffea arabica', 'de', 'German', 'Kaffee', 'Latin', '2026-06-26 15:48:13'),
    (636, 'Coffea arabica', 'it', 'Italian', 'Caffè', 'Native', '2026-06-26 15:48:13'),
    (637, 'Coffea arabica', 'ru', 'Russian', 'Kofe (кофе)', 'Native', '2026-06-26 15:48:13'),
    (638, 'Coffea arabica', 'tr', 'Turkish', 'Kahve', 'Latin', '2026-06-26 15:48:13'),
    (639, 'Camellia sinensis', 'en', 'English', 'Tea', 'Latin', '2026-06-26 15:48:13'),
    (640, 'Camellia sinensis', 'hi', 'Hindi', 'Chai (चाय)', 'Native', '2026-06-26 15:48:13'),
    (641, 'Camellia sinensis', 'bn', 'Bengali', 'Cha (চা)', 'Native', '2026-06-26 15:48:13'),
    (642, 'Camellia sinensis', 'te', 'Telugu', 'Tea (టీ)', 'Native', '2026-06-26 15:48:13'),
    (643, 'Camellia sinensis', 'ta', 'Tamil', 'Theneer (தேயிலை)', 'Native', '2026-06-26 15:48:13'),
    (644, 'Camellia sinensis', 'kn', 'Kannada', 'Tea (ಚಹಾ)', 'Native', '2026-06-26 15:48:13'),
    (645, 'Camellia sinensis', 'ml', 'Malayalam', 'Chaya (ചായ)', 'Native', '2026-06-26 15:48:13'),
    (646, 'Camellia sinensis', 'mr', 'Marathi', 'Chai (चहा)', 'Native', '2026-06-26 15:48:13'),
    (647, 'Camellia sinensis', 'pa', 'Punjabi', 'Chai (ਚਾਹ)', 'Native', '2026-06-26 15:48:13'),
    (648, 'Camellia sinensis', 'ar', 'Arabic', 'Shay (شاي)', 'Native', '2026-06-26 15:48:13'),
    (649, 'Camellia sinensis', 'zh', 'Chinese (Mandarin)', 'Chá (茶)', 'Native', '2026-06-26 15:48:13'),
    (650, 'Camellia sinensis', 'ja', 'Japanese', 'Cha (お茶)', 'Native', '2026-06-26 15:48:13'),
    (651, 'Camellia sinensis', 'ko', 'Korean', 'Cha (차)', 'Native', '2026-06-26 15:48:13'),
    (652, 'Camellia sinensis', 'vi', 'Vietnamese', 'Trà', 'Latin', '2026-06-26 15:48:13'),
    (653, 'Camellia sinensis', 'th', 'Thai', 'Cha (ชา)', 'Native', '2026-06-26 15:48:13'),
    (654, 'Camellia sinensis', 'id', 'Indonesian', 'Teh', 'Latin', '2026-06-26 15:48:13'),
    (655, 'Camellia sinensis', 'ms', 'Malay', 'Teh', 'Latin', '2026-06-26 15:48:13'),
    (656, 'Camellia sinensis', 'tl', 'Filipino (Tagalog)', 'Tsaa', 'Latin', '2026-06-26 15:48:13'),
    (657, 'Camellia sinensis', 'sw', 'Swahili', 'Chai', 'Latin', '2026-06-26 15:48:13'),
    (658, 'Camellia sinensis', 'am', 'Amharic', 'Shai (ሻይ)', 'Native', '2026-06-26 15:48:13'),
    (659, 'Camellia sinensis', 'pt', 'Portuguese', 'Chá', 'Latin', '2026-06-26 15:48:13'),
    (660, 'Camellia sinensis', 'es', 'Spanish', 'Té', 'Latin', '2026-06-26 15:48:13'),
    (661, 'Camellia sinensis', 'fr', 'French', 'Thé', 'Latin', '2026-06-26 15:48:13'),
    (662, 'Camellia sinensis', 'de', 'German', 'Tee', 'Latin', '2026-06-26 15:48:13'),
    (663, 'Camellia sinensis', 'it', 'Italian', 'Tè', 'Native', '2026-06-26 15:48:13'),
    (664, 'Camellia sinensis', 'ru', 'Russian', 'Chay (чай)', 'Native', '2026-06-26 15:48:13'),
    (665, 'Camellia sinensis', 'tr', 'Turkish', 'Çay', 'Latin', '2026-06-26 15:48:13'),
    (666, 'Azadirachta indica', 'en', 'English', 'Neem', 'Latin', '2026-06-26 15:48:13'),
    (667, 'Azadirachta indica', 'hi', 'Hindi', 'Neem (नीम)', 'Native', '2026-06-26 15:48:13'),
    (668, 'Azadirachta indica', 'bn', 'Bengali', 'Neem (নিম)', 'Native', '2026-06-26 15:48:13'),
    (669, 'Azadirachta indica', 'te', 'Telugu', 'Vepa (వేప)', 'Native', '2026-06-26 15:48:13'),
    (670, 'Azadirachta indica', 'ta', 'Tamil', 'Vembu (வேம்பு)', 'Native', '2026-06-26 15:48:13'),
    (671, 'Azadirachta indica', 'kn', 'Kannada', 'Bevu (ಬೇವು)', 'Native', '2026-06-26 15:48:13'),
    (672, 'Azadirachta indica', 'ml', 'Malayalam', 'Veppam (വേപ്പ്)', 'Native', '2026-06-26 15:48:13'),
    (673, 'Azadirachta indica', 'mr', 'Marathi', 'Kadu Limb (कडुलिंब)', 'Native', '2026-06-26 15:48:13'),
    (674, 'Azadirachta indica', 'pa', 'Punjabi', 'Neem (ਨਿੰਮ)', 'Native', '2026-06-26 15:48:13'),
    (675, 'Azadirachta indica', 'gu', 'Gujarati', 'Limado (લીમડો)', 'Native', '2026-06-26 15:48:13'),
    (676, 'Azadirachta indica', 'ur', 'Urdu', 'Neem (نیم)', 'Native', '2026-06-26 15:48:13'),
    (677, 'Azadirachta indica', 'ar', 'Arabic', 'Neem (ليمون مر)', 'Native', '2026-06-26 15:48:13'),
    (678, 'Azadirachta indica', 'sw', 'Swahili', 'Mwarobaini', 'Latin', '2026-06-26 15:48:13'),
    (679, 'Azadirachta indica', 'ha', 'Hausa', 'Dogonyaro', 'Latin', '2026-06-26 15:48:13'),
    (680, 'Azadirachta indica', 'yo', 'Yoruba', 'Dongoyaro', 'Latin', '2026-06-26 15:48:13'),
    (681, 'Azadirachta indica', 'pt', 'Portuguese', 'Nim', 'Latin', '2026-06-26 15:48:13'),
    (682, 'Azadirachta indica', 'es', 'Spanish', 'Nim', 'Latin', '2026-06-26 15:48:13'),
    (683, 'Azadirachta indica', 'fr', 'French', 'Margousier', 'Latin', '2026-06-26 15:48:13'),
    (684, 'Azadirachta indica', 'de', 'German', 'Niembaum', 'Latin', '2026-06-26 15:48:13'),
    (685, 'Azadirachta indica', 'ms', 'Malay', 'Pokok neem', 'Latin', '2026-06-26 15:48:13'),
    (686, 'Azadirachta indica', 'id', 'Indonesian', 'Pohon neem', 'Latin', '2026-06-26 15:48:13'),
    (687, 'Ocimum tenuiflorum', 'en', 'English', 'Tulsi / Holy Basil', 'Latin', '2026-06-26 15:48:13'),
    (688, 'Ocimum tenuiflorum', 'hi', 'Hindi', 'Tulsi (तुलसी)', 'Native', '2026-06-26 15:48:13'),
    (689, 'Ocimum tenuiflorum', 'bn', 'Bengali', 'Tulsi (তুলসী)', 'Native', '2026-06-26 15:48:13'),
    (690, 'Ocimum tenuiflorum', 'te', 'Telugu', 'Tulasi (తులసి)', 'Native', '2026-06-26 15:48:13'),
    (691, 'Ocimum tenuiflorum', 'ta', 'Tamil', 'Thulasi (துளசி)', 'Native', '2026-06-26 15:48:13'),
    (692, 'Ocimum tenuiflorum', 'kn', 'Kannada', 'Tulasi (ತುಳಸಿ)', 'Native', '2026-06-26 15:48:13'),
    (693, 'Ocimum tenuiflorum', 'ml', 'Malayalam', 'Thulasi (തുളസി)', 'Native', '2026-06-26 15:48:13'),
    (694, 'Ocimum tenuiflorum', 'mr', 'Marathi', 'Tulashi (तुळस)', 'Native', '2026-06-26 15:48:13'),
    (695, 'Ocimum tenuiflorum', 'pa', 'Punjabi', 'Tulsi (ਤੁਲਸੀ)', 'Native', '2026-06-26 15:48:13'),
    (696, 'Ocimum tenuiflorum', 'gu', 'Gujarati', 'Tulsi (તુલસી)', 'Native', '2026-06-26 15:48:13'),
    (697, 'Ocimum tenuiflorum', 'ur', 'Urdu', 'Tulsi (تلسی)', 'Native', '2026-06-26 15:48:13'),
    (698, 'Ocimum tenuiflorum', 'si', 'Sinhala', 'Tulasi (තුළසි)', 'Native', '2026-06-26 15:48:13'),
    (699, 'Ocimum tenuiflorum', 'ne', 'Nepali', 'Tulsi (तुलसी)', 'Native', '2026-06-26 15:48:13'),
    (700, 'Ocimum tenuiflorum', 'th', 'Thai', 'Kraphao (กะเพรา)', 'Native', '2026-06-26 15:48:13');
INSERT INTO multilingual_names (id, botanical_name, language_code, language_name, local_name, script, created_at) VALUES
    (701, 'Ocimum tenuiflorum', 'id', 'Indonesian', 'Kemangi', 'Latin', '2026-06-26 15:48:13'),
    (702, 'Ocimum tenuiflorum', 'ms', 'Malay', 'Selasih', 'Latin', '2026-06-26 15:48:13'),
    (703, 'Withania somnifera', 'en', 'English', 'Ashwagandha / Indian Ginseng', 'Latin', '2026-06-26 15:48:13'),
    (704, 'Withania somnifera', 'hi', 'Hindi', 'Ashwagandha (अश्वगंधा)', 'Native', '2026-06-26 15:48:13'),
    (705, 'Withania somnifera', 'bn', 'Bengali', 'Ashwagandha (অশ্বগন্ধা)', 'Native', '2026-06-26 15:48:13'),
    (706, 'Withania somnifera', 'te', 'Telugu', 'Aswagandha (అశ్వగంధ)', 'Native', '2026-06-26 15:48:13'),
    (707, 'Withania somnifera', 'ta', 'Tamil', 'Amukkara (அமுக்கரா)', 'Native', '2026-06-26 15:48:13'),
    (708, 'Withania somnifera', 'kn', 'Kannada', 'Ashwagandha (ಅಶ್ವಗಂಧ)', 'Native', '2026-06-26 15:48:13'),
    (709, 'Withania somnifera', 'ml', 'Malayalam', 'Amukkuram (അമുക്കുരം)', 'Native', '2026-06-26 15:48:13'),
    (710, 'Withania somnifera', 'mr', 'Marathi', 'Ashwagandha (अश्वगंधा)', 'Native', '2026-06-26 15:48:13'),
    (711, 'Withania somnifera', 'ur', 'Urdu', 'Asgandh (اشواگندھ)', 'Native', '2026-06-26 15:48:13'),
    (712, 'Withania somnifera', 'ar', 'Arabic', 'Ashwagandha (أشواغاندا)', 'Native', '2026-06-26 15:48:13'),
    (713, 'Withania somnifera', 'zh', 'Chinese (Mandarin)', 'Nan fei zui qie (南非醉茄)', 'Native', '2026-06-26 15:48:13'),
    (714, 'Aloe vera', 'en', 'English', 'Aloe Vera', 'Latin', '2026-06-26 15:48:13'),
    (715, 'Aloe vera', 'hi', 'Hindi', 'Ghritkumari (घृतकुमारी)', 'Native', '2026-06-26 15:48:13'),
    (716, 'Aloe vera', 'bn', 'Bengali', 'Aloe Vera (অ্যালোভেরা)', 'Native', '2026-06-26 15:48:13'),
    (717, 'Aloe vera', 'te', 'Telugu', 'Kalabanda (కలబంద)', 'Native', '2026-06-26 15:48:13'),
    (718, 'Aloe vera', 'ta', 'Tamil', 'Sotrukatralai (சோற்றுக் கற்றாழை)', 'Native', '2026-06-26 15:48:13'),
    (719, 'Aloe vera', 'kn', 'Kannada', 'Lolesara (ಲೋಳೆ ಸಾರ)', 'Native', '2026-06-26 15:48:13'),
    (720, 'Aloe vera', 'ml', 'Malayalam', 'Kuthamb (കൂടം)', 'Native', '2026-06-26 15:48:13'),
    (721, 'Aloe vera', 'mr', 'Marathi', 'Korphad (कोरफड)', 'Native', '2026-06-26 15:48:13'),
    (722, 'Aloe vera', 'pa', 'Punjabi', 'Aloe (ਐਲੋਵੇਰਾ)', 'Native', '2026-06-26 15:48:13'),
    (723, 'Aloe vera', 'gu', 'Gujarati', 'Kumari (કુંવાર)', 'Native', '2026-06-26 15:48:13'),
    (724, 'Aloe vera', 'ar', 'Arabic', 'Sabbar (صبار)', 'Native', '2026-06-26 15:48:13'),
    (725, 'Aloe vera', 'zh', 'Chinese (Mandarin)', 'Lúhuì (芦荟)', 'Native', '2026-06-26 15:48:13'),
    (726, 'Aloe vera', 'ja', 'Japanese', 'Aloe (アロエ)', 'Native', '2026-06-26 15:48:13'),
    (727, 'Aloe vera', 'th', 'Thai', 'Wan hang chorakhe (ว่านหางจระเข้)', 'Native', '2026-06-26 15:48:13'),
    (728, 'Aloe vera', 'id', 'Indonesian', 'Lidah buaya', 'Latin', '2026-06-26 15:48:13'),
    (729, 'Aloe vera', 'ms', 'Malay', 'Pokok Aloe Vera', 'Latin', '2026-06-26 15:48:13'),
    (730, 'Aloe vera', 'sw', 'Swahili', 'Aloe', 'Latin', '2026-06-26 15:48:13'),
    (731, 'Aloe vera', 'pt', 'Portuguese', 'Babosa', 'Latin', '2026-06-26 15:48:13'),
    (732, 'Aloe vera', 'es', 'Spanish', 'Sábila', 'Latin', '2026-06-26 15:48:13'),
    (733, 'Aloe vera', 'fr', 'French', 'Aloe', 'Latin', '2026-06-26 15:48:13'),
    (734, 'Aloe vera', 'de', 'German', 'Aloe', 'Latin', '2026-06-26 15:48:13'),
    (735, 'Aloe vera', 'it', 'Italian', 'Aloe vera', 'Native', '2026-06-26 15:48:13'),
    (736, 'Moringa oleifera', 'en', 'English', 'Moringa / Drumstick Tree', 'Latin', '2026-06-26 15:48:13'),
    (737, 'Moringa oleifera', 'hi', 'Hindi', 'Sahjan (सहजन)', 'Native', '2026-06-26 15:48:13'),
    (738, 'Moringa oleifera', 'bn', 'Bengali', 'Sajna (সজনে)', 'Native', '2026-06-26 15:48:13'),
    (739, 'Moringa oleifera', 'te', 'Telugu', 'Mulaga (మునగ)', 'Native', '2026-06-26 15:48:13'),
    (740, 'Moringa oleifera', 'ta', 'Tamil', 'Murungai (முருங்கை)', 'Native', '2026-06-26 15:48:13'),
    (741, 'Moringa oleifera', 'kn', 'Kannada', 'Nugge (ನುಗ್ಗೆ)', 'Native', '2026-06-26 15:48:13'),
    (742, 'Moringa oleifera', 'ml', 'Malayalam', 'Muringa (മുരിങ്ങ)', 'Native', '2026-06-26 15:48:13'),
    (743, 'Moringa oleifera', 'mr', 'Marathi', 'Shevga (शेवगा)', 'Native', '2026-06-26 15:48:13'),
    (744, 'Moringa oleifera', 'pa', 'Punjabi', 'Sohanjana (ਸਹਿਜਣਾ)', 'Native', '2026-06-26 15:48:13'),
    (745, 'Moringa oleifera', 'gu', 'Gujarati', 'Saragvo (સરગવો)', 'Native', '2026-06-26 15:48:13'),
    (746, 'Moringa oleifera', 'ur', 'Urdu', 'Sahjan (سہجن)', 'Native', '2026-06-26 15:48:13'),
    (747, 'Moringa oleifera', 'ar', 'Arabic', 'Rawaq (رواق)', 'Native', '2026-06-26 15:48:13'),
    (748, 'Moringa oleifera', 'zh', 'Chinese (Mandarin)', 'Lamu ye (辣木)', 'Native', '2026-06-26 15:48:13'),
    (749, 'Moringa oleifera', 'sw', 'Swahili', 'Mzungu (Moringa)', 'Latin', '2026-06-26 15:48:13'),
    (750, 'Moringa oleifera', 'ha', 'Hausa', 'Zogale', 'Latin', '2026-06-26 15:48:13'),
    (751, 'Moringa oleifera', 'yo', 'Yoruba', 'Igbale Ogangun', 'Latin', '2026-06-26 15:48:13'),
    (752, 'Moringa oleifera', 'am', 'Amharic', 'Shiferaw (ሽፌራ)', 'Native', '2026-06-26 15:48:13'),
    (753, 'Moringa oleifera', 'pt', 'Portuguese', 'Moringa', 'Latin', '2026-06-26 15:48:13'),
    (754, 'Moringa oleifera', 'es', 'Spanish', 'Moringa', 'Latin', '2026-06-26 15:48:13'),
    (755, 'Moringa oleifera', 'fr', 'French', 'Moringa', 'Latin', '2026-06-26 15:48:13'),
    (756, 'Moringa oleifera', 'de', 'German', 'Moringa', 'Latin', '2026-06-26 15:48:13'),
    (757, 'Nelumbo nucifera', 'en', 'English', 'Lotus', 'Latin', '2026-06-26 15:48:13'),
    (758, 'Nelumbo nucifera', 'hi', 'Hindi', 'Kamal (कमल)', 'Native', '2026-06-26 15:48:13'),
    (759, 'Nelumbo nucifera', 'bn', 'Bengali', 'Padma (পদ্ম)', 'Native', '2026-06-26 15:48:13'),
    (760, 'Nelumbo nucifera', 'te', 'Telugu', 'Thamara (తామర)', 'Native', '2026-06-26 15:48:13'),
    (761, 'Nelumbo nucifera', 'ta', 'Tamil', 'Tamara (தாமரை)', 'Native', '2026-06-26 15:48:13'),
    (762, 'Nelumbo nucifera', 'kn', 'Kannada', 'Thamara (ತಾವರೆ)', 'Native', '2026-06-26 15:48:13'),
    (763, 'Nelumbo nucifera', 'ml', 'Malayalam', 'Thamara (താമര)', 'Native', '2026-06-26 15:48:13'),
    (764, 'Nelumbo nucifera', 'mr', 'Marathi', 'Kamal (कमळ)', 'Native', '2026-06-26 15:48:13'),
    (765, 'Nelumbo nucifera', 'pa', 'Punjabi', 'Kamal (ਕਮਲ)', 'Native', '2026-06-26 15:48:13'),
    (766, 'Nelumbo nucifera', 'gu', 'Gujarati', 'Kamal (કમળ)', 'Native', '2026-06-26 15:48:13'),
    (767, 'Nelumbo nucifera', 'ur', 'Urdu', 'Kamal (کنول)', 'Native', '2026-06-26 15:48:13'),
    (768, 'Nelumbo nucifera', 'ar', 'Arabic', 'Lotus (لوتس)', 'Native', '2026-06-26 15:48:13'),
    (769, 'Nelumbo nucifera', 'zh', 'Chinese (Mandarin)', 'Héhuā (荷花)', 'Native', '2026-06-26 15:48:13'),
    (770, 'Nelumbo nucifera', 'ja', 'Japanese', 'Hasu (ハス)', 'Native', '2026-06-26 15:48:13'),
    (771, 'Nelumbo nucifera', 'ko', 'Korean', 'Yeonkkot (연꽃)', 'Native', '2026-06-26 15:48:13'),
    (772, 'Nelumbo nucifera', 'vi', 'Vietnamese', 'Hoa sen', 'Latin', '2026-06-26 15:48:13'),
    (773, 'Nelumbo nucifera', 'th', 'Thai', 'Bua (บัว)', 'Native', '2026-06-26 15:48:13'),
    (774, 'Nelumbo nucifera', 'id', 'Indonesian', 'Lotus', 'Latin', '2026-06-26 15:48:13'),
    (775, 'Nelumbo nucifera', 'ms', 'Malay', 'Bunga teratai', 'Latin', '2026-06-26 15:48:13'),
    (776, 'Nelumbo nucifera', 'tl', 'Filipino (Tagalog)', 'Lotus', 'Latin', '2026-06-26 15:48:13'),
    (777, 'Phyllanthus emblica', 'en', 'English', 'Indian Gooseberry (Amla)', 'Latin', '2026-06-26 15:48:13'),
    (778, 'Phyllanthus emblica', 'hi', 'Hindi', 'Amla (आंवला)', 'Native', '2026-06-26 15:48:13'),
    (779, 'Phyllanthus emblica', 'bn', 'Bengali', 'Amloki (আমলকী)', 'Native', '2026-06-26 15:48:13'),
    (780, 'Phyllanthus emblica', 'te', 'Telugu', 'Usirika (ఉసిరిక)', 'Native', '2026-06-26 15:48:13'),
    (781, 'Phyllanthus emblica', 'ta', 'Tamil', 'Nelli (நெல்லி)', 'Native', '2026-06-26 15:48:13'),
    (782, 'Phyllanthus emblica', 'kn', 'Kannada', 'Nelli (ನೆಲ್ಲಿ)', 'Native', '2026-06-26 15:48:13'),
    (783, 'Phyllanthus emblica', 'ml', 'Malayalam', 'Nellikka (നെല്ലിക്ക)', 'Native', '2026-06-26 15:48:13'),
    (784, 'Phyllanthus emblica', 'mr', 'Marathi', 'Avla (आवळा)', 'Native', '2026-06-26 15:48:13'),
    (785, 'Phyllanthus emblica', 'pa', 'Punjabi', 'Amla (ਆਂਵਲਾ)', 'Native', '2026-06-26 15:48:13'),
    (786, 'Phyllanthus emblica', 'gu', 'Gujarati', 'Amla (આમળ)', 'Native', '2026-06-26 15:48:13'),
    (787, 'Phyllanthus emblica', 'ur', 'Urdu', 'Amla (آملہ)', 'Native', '2026-06-26 15:48:13'),
    (788, 'Phyllanthus emblica', 'ar', 'Arabic', 'Usaira', 'Native', '2026-06-26 15:48:13'),
    (789, 'Phyllanthus emblica', 'zh', 'Chinese (Mandarin)', 'Yu gan zi (余甘子)', 'Native', '2026-06-26 15:48:13'),
    (790, 'Phyllanthus emblica', 'th', 'Thai', 'Ma kham pom (มะขามป้อม)', 'Native', '2026-06-26 15:48:13'),
    (791, 'Phyllanthus emblica', 'id', 'Indonesian', 'Amla', 'Latin', '2026-06-26 15:48:13'),
    (792, 'Phyllanthus emblica', 'ms', 'Malay', 'Pokok melaka', 'Latin', '2026-06-26 15:48:13'),
    (793, 'Phyllanthus emblica', 'sw', 'Swahili', 'Amla', 'Latin', '2026-06-26 15:48:13'),
    (794, 'Hibiscus rosa-sinensis', 'en', 'English', 'Hibiscus / China Rose', 'Latin', '2026-06-26 15:48:13'),
    (795, 'Hibiscus rosa-sinensis', 'hi', 'Hindi', 'Gurhal (गुड़हल)', 'Native', '2026-06-26 15:48:13'),
    (796, 'Hibiscus rosa-sinensis', 'bn', 'Bengali', 'Jaba (জবা)', 'Native', '2026-06-26 15:48:13'),
    (797, 'Hibiscus rosa-sinensis', 'te', 'Telugu', 'Dasana puvvu (దాసాని పువ్వు)', 'Native', '2026-06-26 15:48:13'),
    (798, 'Hibiscus rosa-sinensis', 'ta', 'Tamil', 'Sembaruthi (செம்பருத்தி)', 'Native', '2026-06-26 15:48:13'),
    (799, 'Hibiscus rosa-sinensis', 'kn', 'Kannada', 'Daasavala (ದಾಸವಾಳ)', 'Native', '2026-06-26 15:48:13'),
    (800, 'Hibiscus rosa-sinensis', 'ml', 'Malayalam', 'Chembarathi (ചെമ്പരത്തി)', 'Native', '2026-06-26 15:48:13');
INSERT INTO multilingual_names (id, botanical_name, language_code, language_name, local_name, script, created_at) VALUES
    (801, 'Hibiscus rosa-sinensis', 'mr', 'Marathi', 'Jaswand (जास्वंद)', 'Native', '2026-06-26 15:48:13'),
    (802, 'Hibiscus rosa-sinensis', 'pa', 'Punjabi', 'Gurhal (ਗੁੜਹਲ)', 'Native', '2026-06-26 15:48:13'),
    (803, 'Hibiscus rosa-sinensis', 'gu', 'Gujarati', 'Jasood (જાસૂ)', 'Native', '2026-06-26 15:48:13'),
    (804, 'Hibiscus rosa-sinensis', 'ur', 'Urdu', 'Gurhal (گلاب چین)', 'Native', '2026-06-26 15:48:13'),
    (805, 'Hibiscus rosa-sinensis', 'ar', 'Arabic', 'Karkadeh (كركديه)', 'Native', '2026-06-26 15:48:13'),
    (806, 'Hibiscus rosa-sinensis', 'zh', 'Chinese (Mandarin)', 'Fúsāng (扶桑)', 'Native', '2026-06-26 15:48:13'),
    (807, 'Hibiscus rosa-sinensis', 'ja', 'Japanese', 'Hibiscus (ハイビスカス)', 'Native', '2026-06-26 15:48:13'),
    (808, 'Hibiscus rosa-sinensis', 'ko', 'Korean', 'Hibiscus (히비스커스)', 'Native', '2026-06-26 15:48:13'),
    (809, 'Hibiscus rosa-sinensis', 'vi', 'Vietnamese', 'Râm bụt', 'Latin', '2026-06-26 15:48:13'),
    (810, 'Hibiscus rosa-sinensis', 'th', 'Thai', 'Chaba (ชบา)', 'Native', '2026-06-26 15:48:13'),
    (811, 'Hibiscus rosa-sinensis', 'id', 'Indonesian', 'Kembang sepatu', 'Latin', '2026-06-26 15:48:13'),
    (812, 'Hibiscus rosa-sinensis', 'ms', 'Malay', 'Bunga raya', 'Latin', '2026-06-26 15:48:13'),
    (813, 'Hibiscus rosa-sinensis', 'tl', 'Filipino (Tagalog)', 'Gumamela', 'Latin', '2026-06-26 15:48:13'),
    (814, 'Psidium guajava', 'en', 'English', 'Guava', 'Latin', '2026-06-26 15:48:13'),
    (815, 'Psidium guajava', 'hi', 'Hindi', 'Amrood (अमरूद)', 'Native', '2026-06-26 15:48:13'),
    (816, 'Psidium guajava', 'bn', 'Bengali', 'Peyara (পেয়ারা)', 'Native', '2026-06-26 15:48:13'),
    (817, 'Psidium guajava', 'te', 'Telugu', 'Jamma (జామ)', 'Native', '2026-06-26 15:48:13'),
    (818, 'Psidium guajava', 'ta', 'Tamil', 'Koyya (கொய்யா)', 'Native', '2026-06-26 15:48:13'),
    (819, 'Psidium guajava', 'kn', 'Kannada', 'Seeba (ಸೀಬೆ)', 'Native', '2026-06-26 15:48:13'),
    (820, 'Psidium guajava', 'ml', 'Malayalam', 'Pera (പേര)', 'Native', '2026-06-26 15:48:13'),
    (821, 'Psidium guajava', 'mr', 'Marathi', 'Peron (पेरू)', 'Native', '2026-06-26 15:48:13'),
    (822, 'Psidium guajava', 'pa', 'Punjabi', 'Amrood (ਅਮਰੂਦ)', 'Native', '2026-06-26 15:48:13'),
    (823, 'Psidium guajava', 'gu', 'Gujarati', 'Jamfal (જામફળ)', 'Native', '2026-06-26 15:48:13'),
    (824, 'Psidium guajava', 'ur', 'Urdu', 'Amrood (امرود)', 'Native', '2026-06-26 15:48:13'),
    (825, 'Psidium guajava', 'ar', 'Arabic', 'Gawaafa (جوافة)', 'Native', '2026-06-26 15:48:13'),
    (826, 'Psidium guajava', 'zh', 'Chinese (Mandarin)', 'Fānshíliu (番石榴)', 'Native', '2026-06-26 15:48:13'),
    (827, 'Psidium guajava', 'ja', 'Japanese', 'Guava (グアバ)', 'Native', '2026-06-26 15:48:13'),
    (828, 'Psidium guajava', 'ko', 'Korean', 'Guava (구아바)', 'Native', '2026-06-26 15:48:13'),
    (829, 'Psidium guajava', 'vi', 'Vietnamese', 'Ổi', 'Latin', '2026-06-26 15:48:13'),
    (830, 'Psidium guajava', 'th', 'Thai', 'Farang (ฝรั่ง)', 'Native', '2026-06-26 15:48:13'),
    (831, 'Psidium guajava', 'id', 'Indonesian', 'Jambu biji', 'Latin', '2026-06-26 15:48:13'),
    (832, 'Psidium guajava', 'ms', 'Malay', 'Jambu batu', 'Latin', '2026-06-26 15:48:13'),
    (833, 'Psidium guajava', 'tl', 'Filipino (Tagalog)', 'Bayabas', 'Latin', '2026-06-26 15:48:13'),
    (834, 'Psidium guajava', 'sw', 'Swahili', 'Mapera', 'Latin', '2026-06-26 15:48:13'),
    (835, 'Psidium guajava', 'ha', 'Hausa', 'Gwaba', 'Latin', '2026-06-26 15:48:13'),
    (836, 'Psidium guajava', 'yo', 'Yoruba', 'Guava', 'Latin', '2026-06-26 15:48:13'),
    (837, 'Psidium guajava', 'pt', 'Portuguese', 'Goiaba', 'Latin', '2026-06-26 15:48:13'),
    (838, 'Psidium guajava', 'es', 'Spanish', 'Guayaba', 'Latin', '2026-06-26 15:48:13'),
    (839, 'Psidium guajava', 'fr', 'French', 'Goyave', 'Latin', '2026-06-26 15:48:13'),
    (840, 'Psidium guajava', 'de', 'German', 'Guave', 'Latin', '2026-06-26 15:48:13'),
    (841, 'Piper nigrum', 'en', 'English', 'Black Pepper', 'Latin', '2026-06-26 15:48:13'),
    (842, 'Piper nigrum', 'hi', 'Hindi', 'Kali Mirch (काली मिर्च)', 'Native', '2026-06-26 15:48:13'),
    (843, 'Piper nigrum', 'bn', 'Bengali', 'Kalo Morich (কালো মরিচ)', 'Native', '2026-06-26 15:48:13'),
    (844, 'Piper nigrum', 'te', 'Telugu', 'Miriyalu (మిరియాలు)', 'Native', '2026-06-26 15:48:13'),
    (845, 'Piper nigrum', 'ta', 'Tamil', 'Milagu (மிளகு)', 'Native', '2026-06-26 15:48:13'),
    (846, 'Piper nigrum', 'kn', 'Kannada', 'Menasu (ಮೆಣಸು)', 'Native', '2026-06-26 15:48:13'),
    (847, 'Piper nigrum', 'ml', 'Malayalam', 'Kurumulaku (കുരുമുളക്)', 'Native', '2026-06-26 15:48:13'),
    (848, 'Piper nigrum', 'mr', 'Marathi', 'Miri (मिरी)', 'Native', '2026-06-26 15:48:13'),
    (849, 'Piper nigrum', 'pa', 'Punjabi', 'Kali Mirch (ਕਾਲੀ ਮਿਰਚ)', 'Native', '2026-06-26 15:48:13'),
    (850, 'Piper nigrum', 'gu', 'Gujarati', 'Mari (મરી)', 'Native', '2026-06-26 15:48:13'),
    (851, 'Piper nigrum', 'ur', 'Urdu', 'Kali Mirch (کالی مرچ)', 'Native', '2026-06-26 15:48:13'),
    (852, 'Piper nigrum', 'ar', 'Arabic', 'Filfil (فلفل أسود)', 'Native', '2026-06-26 15:48:13'),
    (853, 'Piper nigrum', 'zh', 'Chinese (Mandarin)', 'Hēijiāo (黑胡椒)', 'Native', '2026-06-26 15:48:13'),
    (854, 'Piper nigrum', 'ja', 'Japanese', 'Koshō (胡椒)', 'Native', '2026-06-26 15:48:13'),
    (855, 'Piper nigrum', 'ko', 'Korean', 'Hwijang (후추)', 'Native', '2026-06-26 15:48:13'),
    (856, 'Piper nigrum', 'vi', 'Vietnamese', 'Tiêu', 'Latin', '2026-06-26 15:48:13'),
    (857, 'Piper nigrum', 'th', 'Thai', 'Phrik Thai (พริกไทย)', 'Native', '2026-06-26 15:48:13'),
    (858, 'Piper nigrum', 'id', 'Indonesian', 'Lada', 'Latin', '2026-06-26 15:48:13'),
    (859, 'Piper nigrum', 'ms', 'Malay', 'Lada hitam', 'Latin', '2026-06-26 15:48:13'),
    (860, 'Piper nigrum', 'tl', 'Filipino (Tagalog)', 'Paminta', 'Latin', '2026-06-26 15:48:13'),
    (861, 'Piper nigrum', 'sw', 'Swahili', 'Pilipili nyeusi', 'Latin', '2026-06-26 15:48:13'),
    (862, 'Piper nigrum', 'ha', 'Hausa', 'Barkono', 'Latin', '2026-06-26 15:48:13'),
    (863, 'Piper nigrum', 'pt', 'Portuguese', 'Pimenta-do-reino', 'Latin', '2026-06-26 15:48:13'),
    (864, 'Piper nigrum', 'es', 'Spanish', 'Pimienta negra', 'Latin', '2026-06-26 15:48:13'),
    (865, 'Piper nigrum', 'fr', 'French', 'Poivre noir', 'Latin', '2026-06-26 15:48:13'),
    (866, 'Piper nigrum', 'de', 'German', 'Schwarzer Pfeffer', 'Latin', '2026-06-26 15:48:13'),
    (867, 'Piper nigrum', 'it', 'Italian', 'Pepe nero', 'Native', '2026-06-26 15:48:13'),
    (868, 'Piper nigrum', 'ru', 'Russian', 'Chyorny perets (чёрный перец)', 'Native', '2026-06-26 15:48:13'),
    (869, 'Cinnamomum verum', 'en', 'English', 'Cinnamon', 'Latin', '2026-06-26 15:48:13'),
    (870, 'Cinnamomum verum', 'hi', 'Hindi', 'Dalchini (दालचीनी)', 'Native', '2026-06-26 15:48:13'),
    (871, 'Cinnamomum verum', 'bn', 'Bengali', 'Dalchini (দারুচিনি)', 'Native', '2026-06-26 15:48:13'),
    (872, 'Cinnamomum verum', 'te', 'Telugu', 'Dalchini (దాల్చినచెక్క)', 'Native', '2026-06-26 15:48:13'),
    (873, 'Cinnamomum verum', 'ta', 'Tamil', 'Elavangam (இலவங்கம்)', 'Native', '2026-06-26 15:48:13'),
    (874, 'Cinnamomum verum', 'kn', 'Kannada', 'Chakke (ಚಕ್ಕೆ)', 'Native', '2026-06-26 15:48:13'),
    (875, 'Cinnamomum verum', 'ml', 'Malayalam', 'Karuvapatta (കറുവ)', 'Native', '2026-06-26 15:48:13'),
    (876, 'Cinnamomum verum', 'mr', 'Marathi', 'Dalchini (दालचिनी)', 'Native', '2026-06-26 15:48:13'),
    (877, 'Cinnamomum verum', 'pa', 'Punjabi', 'Dalchini (ਦਾਲਚੀਨੀ)', 'Native', '2026-06-26 15:48:13'),
    (878, 'Cinnamomum verum', 'ur', 'Urdu', 'Dalchini (دارچینی)', 'Native', '2026-06-26 15:48:13'),
    (879, 'Cinnamomum verum', 'ar', 'Arabic', 'Qirfa (قرفة)', 'Native', '2026-06-26 15:48:13'),
    (880, 'Cinnamomum verum', 'zh', 'Chinese (Mandarin)', 'Ròuguì (肉桂)', 'Native', '2026-06-26 15:48:13'),
    (881, 'Cinnamomum verum', 'ja', 'Japanese', 'Shinamon (シナモン)', 'Native', '2026-06-26 15:48:13'),
    (882, 'Cinnamomum verum', 'ko', 'Korean', 'Gyepi (계피)', 'Native', '2026-06-26 15:48:13'),
    (883, 'Cinnamomum verum', 'vi', 'Vietnamese', 'Quế', 'Latin', '2026-06-26 15:48:13'),
    (884, 'Cinnamomum verum', 'th', 'Thai', 'Op choei (อบเชย)', 'Native', '2026-06-26 15:48:13'),
    (885, 'Cinnamomum verum', 'id', 'Indonesian', 'Kayu manis', 'Latin', '2026-06-26 15:48:13'),
    (886, 'Cinnamomum verum', 'ms', 'Malay', 'Kayu manis', 'Latin', '2026-06-26 15:48:13'),
    (887, 'Cinnamomum verum', 'tl', 'Filipino (Tagalog)', 'Kanela', 'Latin', '2026-06-26 15:48:13'),
    (888, 'Cinnamomum verum', 'sw', 'Swahili', 'Mdalasini', 'Latin', '2026-06-26 15:48:13'),
    (889, 'Cinnamomum verum', 'pt', 'Portuguese', 'Canela', 'Latin', '2026-06-26 15:48:13'),
    (890, 'Cinnamomum verum', 'es', 'Spanish', 'Canela', 'Latin', '2026-06-26 15:48:13'),
    (891, 'Cinnamomum verum', 'fr', 'French', 'Cannelle', 'Latin', '2026-06-26 15:48:13'),
    (892, 'Cinnamomum verum', 'de', 'German', 'Zimt', 'Latin', '2026-06-26 15:48:13');

DROP TABLE IF EXISTS cultivation_guides CASCADE;
CREATE TABLE cultivation_guides (
    id INTEGER PRIMARY KEY NOT NULL,
    crop_name VARCHAR(200) NOT NULL,
    botanical_name VARCHAR(300) NULL,
    crop_origin VARCHAR(300) NULL,
    climate_type VARCHAR(200) NULL,
    temp_optimum VARCHAR(100) NULL,
    rainfall_requirement VARCHAR(100) NULL,
    soil_type VARCHAR(300) NULL,
    soil_ph_range VARCHAR(50) NULL,
    soil_special_requirements VARCHAR(255) NULL,
    seed_rate VARCHAR(200) NULL,
    spacing VARCHAR(200) NULL,
    irrigation_method VARCHAR(200) NULL,
    irrigation_critical_stages VARCHAR(255) NULL,
    water_requirement_mm VARCHAR(100) NULL,
    npk_recommendation VARCHAR(200) NULL,
    fertilization_schedule VARCHAR(255) NULL,
    harvest_maturity_indicator VARCHAR(255) NULL,
    harvest_method VARCHAR(300) NULL,
    yield_per_ha VARCHAR(200) NULL,
    full_guide_json VARCHAR(255) NULL,
    created_at TIMESTAMP NULL
);

-- Data for cultivation_guides (11 rows)
INSERT INTO cultivation_guides (id, crop_name, botanical_name, crop_origin, climate_type, temp_optimum, rainfall_requirement, soil_type, soil_ph_range, soil_special_requirements, seed_rate, spacing, irrigation_method, irrigation_critical_stages, water_requirement_mm, npk_recommendation, fertilization_schedule, harvest_maturity_indicator, harvest_method, yield_per_ha, full_guide_json, created_at) VALUES
    (1, 'Rice', 'Oryza sativa', 'Southeast Asia (China-India border region)', 'Tropical and subtropical', '21-37°C (germination 18-40°C)', '1000-2000mm annual; most during growing season', 'Heavy clay or clay-loam soils with good water retention', '5.0-7.0 (optimal 6.0-6.5)', 'Impermeable clay layer needed for paddy cultivation; good drainage for upland rice', 'Transplanted: 25-30 kg/ha; Direct seeded: 80-100 kg/ha', '20×15 cm or 20×20 cm; 2-3 seedlings per hill', 'Continuous flooding (5-7cm standing water) in paddy field', 'Tillering, panicle initiation, and flowering', '1000-2000mm total', 'N120-P60-K60 for irrigated HYV', 'Basal: 50%N+100%P+50%K; Topdressing: 25%N at tillering + 25%N at PI', '85-90% grain golden yellow; moisture content 20-25%', 'Reaping by sickle or combine harvester', '3-8 t/ha (irrigated HYV); 1-2 t/ha (rainfed)', '{"botanical_name": "Oryza sativa", "origin": "Southeast Asia (China-India border region)", "climate": {"type": "Tropical and subtropical", "temp_optimum_C": "21-37\u00b0C (germination 18-40\u00b0C)", "rainfall_mm": "1000-2000mm annual; most during growing season", "humidity": "High humidity preferred", "altitude_m": "0-2000m (lowland to highland varieties)"}, "soil": {"type": "Heavy clay or clay-loam soils with good water retention", "ph_range": "5.0-7.0 (optimal 6.0-6.5)", "special_requirements": "Impermeable clay layer needed for paddy cultivation; good drainage for upland rice", "avoid": "Sandy or gravelly soils for irrigated paddy"}, "seasons": {"kharif_India": "June-November (Sown June-July, Harvested Oct-Nov)", "rabi_India": "November-March (some areas)", "tropical": "Can be grown year-round with irrigation"}, "varieties": {"IR64": "Irrigated lowland, 110 days, 5-6 t/ha", "Swarna_Sub1": "Flood-tolerant, 130 days, submergence-resistant", "BPT_5204": "Samba Masuri, aromatic, popular in Andhra Pradesh", "Basmati_370": "Long-grain aromatic, export quality, Pakistan/India", "NERICA": "Upland rice for Africa, drought-tolerant"}, "seed_rate": "Transplanted: 25-30 kg/ha; Direct seeded: 80-100 kg/ha", "nursery": "Raise seedlings in nursery for 25-30 days; transplant at 2-3 leaf stage", "spacing": "20\u00d715 cm or 20\u00d720 cm; 2-3 seedlings per hill", "irrigation": {"method": "Continuous flooding (5-7cm standing water) in paddy field", "critical_stages": "Tillering, panicle initiation, and flowering", "AWD": "Alternate Wetting and Drying (AWD) saves 25-30% water; maintain 15cm depth markers", "water_requirement_mm": "1000-2000mm total"}, "fertilization": {"npk_kg_ha": "N120-P60-K60 for irrigated HYV", "schedule": "Basal: 50%N+100%P+50%K; Topdressing: 25%N at tillering + 25%N at PI", "zinc": "ZnSO4 25 kg/ha basal if deficient; seedling dip 2% ZnSO4", "organic": "FYM 10 t/ha or Dhaincha green manure"}, "weed_management": {"critical_period": "0-45 days after transplanting", "methods": "Hand weeding 20 and 40 DAT; Mechanical weeder (cono-weeder); Herbicides", "herbicides": "Pendimethalin 30 EC (1kg ai/ha) pre-emergence; Bispyribac-sodium (Nominee Gold) at 3-4 leaf stage of weeds", "water_management": "Maintain standing water \u2014 effective weed suppression in paddy"}, "harvesting": {"maturity_indicator": "85-90% grain golden yellow; moisture content 20-25%", "method": "Reaping by sickle or combine harvester", "drying": "Sun dry to 14% moisture for safe storage", "yield_t_ha": "3-8 t/ha (irrigated HYV); 1-2 t/ha (rainfed)"}, "post_harvest": {"threshing": "Foot thresher, power thresher, or combine", "milling": "Rubber roll huller removes husk; polisher removes bran", "storage": "Store at 14% moisture in sealed bins or bags; use phosphine fumigation against pests"}, "intercropping": "Rice-fish farming (rice and freshwater fish); Rice-Azolla (nitrogen fixation)"}', '2026-06-26 15:48:13'),
    (2, 'Wheat', 'Triticum aestivum', 'Fertile Crescent (Middle East)', 'Cool temperate to sub-tropical', 'Germination 3-25°C; optimal growth 15-21°C; grain fill 20-25°C', '375-875mm (rabi / winter crop; relies on residual moisture and irrigation)', 'Well-drained fertile loam or clay-loam soils', '6.0-7.5', 'Good aeration; moderate to high organic matter', '100-125 kg/ha (timely sown); 125-150 kg/ha (late sown)', '22.5 cm row spacing (seed drill); broadcast is less preferred', 'Flood/furrow; drip/sprinkler for water efficiency', 'CRI (Crown Root Initiation at 21 DAS), Tillering, Jointing, Flowering, Grain filling', '400-500mm total', 'N120-P60-K40 for HYV; N150 with S15 for better protein', 'Basal: 50%N+100%P+100%K; Topdressing: 25%N at CRI + 25%N at tillering', 'Straw golden yellow; grain hard and moisture 18-20%', 'Combine harvester or manual harvesting + threshing', '3-6 t/ha irrigated; 1.5-2.5 t/ha rainfed', '{"botanical_name": "Triticum aestivum", "origin": "Fertile Crescent (Middle East)", "climate": {"type": "Cool temperate to sub-tropical", "temp_optimum_C": "Germination 3-25\u00b0C; optimal growth 15-21\u00b0C; grain fill 20-25\u00b0C", "rainfall_mm": "375-875mm (rabi / winter crop; relies on residual moisture and irrigation)", "humidity": "Low humidity preferred; high humidity encourages diseases", "altitude_m": "0-3000m"}, "soil": {"type": "Well-drained fertile loam or clay-loam soils", "ph_range": "6.0-7.5", "special_requirements": "Good aeration; moderate to high organic matter", "avoid": "Waterlogged, poorly drained, or highly acidic soils"}, "seasons": {"India": "Rabi crop \u2014 sown October-November; harvested March-April", "temperate": "Winter wheat sown in autumn; harvested summer"}, "varieties": {"HD3086": "India \u2014 high yield 5-7 t/ha; rust resistant", "WH1105": "Northwestern India; heat and drought tolerant", "PBW343": "Punjab, India \u2014 widely grown", "CIMMYT_WT": "International high-yielding varieties"}, "seed_rate": "100-125 kg/ha (timely sown); 125-150 kg/ha (late sown)", "spacing": "22.5 cm row spacing (seed drill); broadcast is less preferred", "irrigation": {"critical_stages": "CRI (Crown Root Initiation at 21 DAS), Tillering, Jointing, Flowering, Grain filling", "irrigations": "4-6 irrigations (timely sown); 6-8 if late sown", "water_requirement_mm": "400-500mm total", "method": "Flood/furrow; drip/sprinkler for water efficiency"}, "fertilization": {"npk_kg_ha": "N120-P60-K40 for HYV; N150 with S15 for better protein", "schedule": "Basal: 50%N+100%P+100%K; Topdressing: 25%N at CRI + 25%N at tillering", "zinc": "ZnSO4 25 kg/ha every 3 years"}, "weed_management": {"critical_period": "30-45 days after sowing", "methods": "Inter-row cultivation or herbicides", "herbicides": "Clodinafop-propargyl (Topik) 0.4kg ai/ha for grassy weeds; 2,4-D for broadleaf weeds at 25-30 DAS"}, "harvesting": {"maturity_indicator": "Straw golden yellow; grain hard and moisture 18-20%", "method": "Combine harvester or manual harvesting + threshing", "yield_t_ha": "3-6 t/ha irrigated; 1.5-2.5 t/ha rainfed"}, "post_harvest": {"threshing": "Power thresher or combine", "storage": "Store at 12% moisture; use sealed bins; fumigate with Aluminium Phosphide", "quality_grade": "Grade based on protein content (11-14% for bread wheat)"}}', '2026-06-26 15:48:13'),
    (3, 'Tomato', 'Solanum lycopersicum', 'South America (Peru-Ecuador region)', 'Warm sub-tropical to temperate', 'Optimal 20-24°C day; 13-17°C night; no frost tolerance', '600-1500mm; avoid during fruiting; ideal with irrigation', 'Well-drained sandy loam to clay loam with good organic matter', '6.0-7.0', 'Good drainage; avoid standing water', '', '75×60cm for indeterminate; 75×45cm for determinate varieties', 'Drip irrigation preferred; avoid overhead (disease); furrow if drip unavailable', 'Transplanting, flowering, fruit development', '600-1200mm total', 'N150-200, P75-100, K150-200', 'Split N and K through fertigation (8-12 splits through season)', '', '', '25-40 t/ha (open-pollinated); 60-100 t/ha (hybrids, drip, greenhouse)', '{"botanical_name": "Solanum lycopersicum", "origin": "South America (Peru-Ecuador region)", "climate": {"type": "Warm sub-tropical to temperate", "temp_optimum_C": "Optimal 20-24\u00b0C day; 13-17\u00b0C night; no frost tolerance", "temp_threshold": "< 10\u00b0C: growth stops; > 38\u00b0C: flower drop; -2\u00b0C: plant death", "rainfall_mm": "600-1500mm; avoid during fruiting; ideal with irrigation", "humidity": "Moderate 60-70%; high humidity promotes disease"}, "soil": {"type": "Well-drained sandy loam to clay loam with good organic matter", "ph_range": "6.0-7.0", "organic_matter": "> 2.5% recommended", "special_requirements": "Good drainage; avoid standing water"}, "seasons": {"tropical": "Year-round with variety selection; dry season preferred", "India": "Kharif (June-Sept), Rabi (Oct-Jan), Summer (Feb-May)"}, "varieties": {"Pusa_Ruby": "Open-pollinated; good for processing; 65-70 days", "Arka_Rakshak": "Hybrid; resistant to TLB, ToLCV; high yield 75-80 t/ha", "Roma_VF": "Processing variety; paste/puree; determinate", "Namdhari_4266": "Cherry tomato hybrid", "Heinz_1350": "Processing tomato; mechanical harvesting compatible"}, "nursery": {"bed_preparation": "Raised beds; sterilize with solarization or formaldehyde", "seed_rate": "200-250g/ha", "duration": "25-35 days; transplant at 5-6 leaf stage", "hardening": "Reduce irrigation 1 week before transplanting"}, "spacing": "75\u00d760cm for indeterminate; 75\u00d745cm for determinate varieties", "staking": "Stake at 30-40cm height for indeterminate varieties; prevents disease, improves quality", "irrigation": {"method": "Drip irrigation preferred; avoid overhead (disease); furrow if drip unavailable", "frequency": "Daily in summer; every 3-4 days during monsoon", "critical_stages": "Transplanting, flowering, fruit development", "water_requirement_mm": "600-1200mm total"}, "fertilization": {"npk_kg_ha": "N150-200, P75-100, K150-200", "schedule": "Split N and K through fertigation (8-12 splits through season)", "calcium": "Calcium nitrate 150 kg/ha through fertigation to prevent BER", "magnesium": "MgSO4 25 kg/ha basal; foliar spray at fruit set"}, "weed_management": {"methods": "Mulching (black plastic HDPE most effective), hand weeding", "herbicides": "Oxyfluorfen 23.5 EC pre-transplanting (1L/ha)"}, "fruit_development": {"pollination": "Self-pollination in field; bumblebees in greenhouse", "flower_to_fruit": "45-50 days for fruit maturity from anthesis"}, "harvesting": {"index": "Breaker stage for long-distance; Fully ripe for local market", "frequency": "Every 3-4 days during peak production", "yield_t_ha": "25-40 t/ha (open-pollinated); 60-100 t/ha (hybrids, drip, greenhouse)"}, "post_harvest": {"storage": "10-13\u00b0C for 14-21 days; ethylene ripening at 18-20\u00b0C", "grading": "Grade by size and color for export; APEDA standards", "processing": "Puree, paste, ketchup, dried, canned"}}', '2026-06-26 15:48:13'),
    (4, 'Potato', 'Solanum tuberosum', 'Andes Mountains, South America', 'Cool temperate', '15-20°C for tuber initiation; growth 18-25°C', '500-700mm', 'Well-drained sandy loam or loam; deep friable soils', '5.2-6.4 (avoids scab at lower pH)', 'Deep tillage for loose soil for tuber expansion', '', '60-75 cm × 15-20 cm (rows × plants)', 'Furrow or drip irrigation', 'Planting, tuber initiation (60-70 DAS), tuber bulking', '500-700mm', 'N180-P100-K200 (high K for quality)', 'All at planting or split with K', 'Vine death; skin doesn''t peel off when rubbed', 'Mechanical digger or manual fork; avoid damage', '20-40 t/ha', '{"botanical_name": "Solanum tuberosum", "origin": "Andes Mountains, South America", "climate": {"type": "Cool temperate", "temp_optimum_C": "15-20\u00b0C for tuber initiation; growth 18-25\u00b0C", "critical": "Frost kills vines; temperatures > 30\u00b0C stop tuber formation", "rainfall_mm": "500-700mm"}, "soil": {"type": "Well-drained sandy loam or loam; deep friable soils", "ph_range": "5.2-6.4 (avoids scab at lower pH)", "special_requirements": "Deep tillage for loose soil for tuber expansion", "avoid": "Heavy clay, waterlogged, very alkaline soils"}, "varieties": {"Kufri_Jyoti": "India \u2014 round, white skin; 90-110 days; 25-35 t/ha", "Kufri_Bahar": "Short-season variety; 60-70 days", "Russet_Burbank": "USA processing variety; high dry matter", "Desiree": "Red-skinned variety; European markets"}, "seed_tubers": {"size": "30-50g per tuber (whole) or cut pieces 50-60g with 2-3 eyes", "seed_rate": "2000-2500 kg/ha", "treatment": "Dust with carbendazim or thiram before planting"}, "spacing": "60-75 cm \u00d7 15-20 cm (rows \u00d7 plants)", "earthing_up": "Earth up 30 and 50 DAS to prevent greening and encourage tuber development", "irrigation": {"critical_stages": "Planting, tuber initiation (60-70 DAS), tuber bulking", "method": "Furrow or drip irrigation", "water_requirement_mm": "500-700mm", "stop": "Stop irrigation 2 weeks before harvest for skin set"}, "fertilization": {"npk_kg_ha": "N180-P100-K200 (high K for quality)", "calcium": "Apply lime if pH < 5.0; gypsum for scab control", "schedule": "All at planting or split with K"}, "harvesting": {"maturity_indicator": "Vine death; skin doesn''t peel off when rubbed", "timing": "90-120 days depending on variety and market", "method": "Mechanical digger or manual fork; avoid damage", "yield_t_ha": "20-40 t/ha"}, "storage": {"temperature": "4\u00b0C for long-term; 10-13\u00b0C for seed tubers", "humidity": "90-95% RH", "pre_storage": "Cure at 15-18\u00b0C for 10-14 days for wound healing"}}', '2026-06-26 15:48:13'),
    (5, 'Mango', 'Mangifera indica', 'Northeast India, Bangladesh, Myanmar', 'Tropical and subtropical', '24-30°C during vegetative growth; cool dry period needed for flowering', '750-2500mm; dry period during flowering and fruiting essential', 'Deep well-drained alluvial/loamy soils', '5.5-7.5', '', '', '', 'Drip irrigation preferred for bearing orchards', '', '', '', '', '', 'Hand-pick with harvesting poles; 2cm stalk retained to prevent sap burn', '', '{"botanical_name": "Mangifera indica", "origin": "Northeast India, Bangladesh, Myanmar", "climate": {"type": "Tropical and subtropical", "temp_optimum_C": "24-30\u00b0C during vegetative growth; cool dry period needed for flowering", "temp_threshold": "< 10\u00b0C for 2-3 months triggers flowering; frost kills young trees", "rainfall_mm": "750-2500mm; dry period during flowering and fruiting essential", "altitude_m": "0-1500m"}, "soil": {"type": "Deep well-drained alluvial/loamy soils", "ph_range": "5.5-7.5", "depth_required_m": "1.5-2m free of hard pan", "avoid": "Waterlogged, saline, or very shallow soils"}, "varieties": {"Alphonso": "India \u2014 ''King of Mangoes''; sweet, rich flavor; Maharashtra", "Dashehari": "Uttar Pradesh, India \u2014 North Indian market; sweet; polyembryonic", "Langra": "India \u2014 greenish skin when ripe; excellent flavor", "Kesar": "Gujarat, India \u2014 saffron colored pulp; GI tag", "Tommy_Atkins": "USA \u2014 red skin; long shelf life; export variety", "Kent": "Low-fiber, sweet; export to Europe", "Sindhuri": "South India \u2014 round shape; sweet"}, "planting": {"spacing": "10\u00d710m (traditional); 5\u00d75m (high density); 2.5\u00d72.5m (ultra-high density)", "season": "June-September (monsoon planting best for establishment)", "pit_size": "1\u00d71\u00d71m; fill with topsoil + FYM 20kg + lime 1kg", "plant_age": "12-18 month old grafted plants"}, "training_pruning": {"initial": "Remove branches below 1m for clear bole", "regular": "After harvest, remove dead, diseased, crossing branches; open center system", "canopy": "Top grafting for variety conversion"}, "flowering": {"season": "November-January in India", "induction": "Cool dry weather; Paclobutrazol (2g/m canopy spread) in high humidity areas", "pollination": "Insects (bees, flies); wind; some need cross-pollination"}, "irrigation": {"young_trees": "Weekly in summer; every 3-4 days in hot weather", "bearing_trees": "Avoid irrigation 2 months before expected flowering; resume at fruit set", "method": "Drip irrigation preferred for bearing orchards"}, "fertilization": {"young_tree_year1": "N25g + P50g + K50g per plant", "bearing_tree": "N1000g + P500g + K1000g per tree per year (split twice \u2014 post-harvest and pre-flowering)", "micronutrients": "ZnSO4 0.5% foliar after harvest; Borax 0.1% at flower bud stage"}, "fruit_drop": {"June_drop": "Natural thinning; reduce with 2,4-D 10ppm or NAA 20ppm at pea-stage", "causes": "Inadequate nutrition, water stress, disease"}, "harvesting": {"maturity_indices": "Specific gravity > 1.01; shoulder development; green to yellow color change at stem end", "method": "Hand-pick with harvesting poles; 2cm stalk retained to prevent sap burn", "yield_tree": "200-300 fruits (60-100 kg) per year for mature tree", "season": "April-June India (variety dependent)"}, "post_harvest": {"sap_burn_prevention": "Immediate field heat removal; dip in cold water + fruit wash", "ripening": "Carbide-free ripening rooms at 23-25\u00b0C; ethephon", "storage": "Preclimacteric: 13\u00b0C for 3-4 weeks", "export": "Hot water treatment (48\u00b0C, 60min) or Vapor Heat Treatment for quarantine"}}', '2026-06-26 15:48:13'),
    (6, 'Cotton', 'Gossypium hirsutum', 'Mesoamerica (Mexico-Central America region)', 'Warm tropical and subtropical', '21-30°C; minimum 15°C for germination', '500-1500mm; distributed throughout growing season', 'Deep loamy or clay-loam ''black cotton soil'' (vertisol) preferred', '5.5-7.0', '', '', '', 'Furrow or drip', 'Germination, flowering, boll development', '', 'N150-P60-K60 for irrigated hybrid Bt cotton', 'Basal: 50%N+100%P+100%K; Top dressing: 25%N at squaring + 25%N at flowering', '', 'Repeated hand-pickings (3-4 pickings as bolls open); mechanical picking in USA', '2000-2500 kg/ha seed cotton (lint yield 700-900 kg/ha)', '{"botanical_name": "Gossypium hirsutum", "origin": "Mesoamerica (Mexico-Central America region)", "climate": {"type": "Warm tropical and subtropical", "temp_optimum_C": "21-30\u00b0C; minimum 15\u00b0C for germination", "frost_tolerance": "Frost kills the crop", "rainfall_mm": "500-1500mm; distributed throughout growing season", "sunshine": "Needs 180+ frost-free days; 7-8 hours sunshine minimum"}, "soil": {"type": "Deep loamy or clay-loam ''black cotton soil'' (vertisol) preferred", "ph_range": "5.5-7.0", "special": "Tolerates some salinity; good for vertisols", "avoid": "Waterlogged soils; coarse sands"}, "varieties": {"Bt_Cotton": "Hybrid with Cry1Ac Bt gene for bollworm resistance; currently dominant", "MCU_5": "Non-Bt, medium fiber; rainfed cultivation", "Shankar_6": "Gujarat, India; medium to long staple", "DCH_32": "South India; long-staple extra long cotton"}, "sowing": {"time": "May-June with pre-monsoon rains; or after monsoon onset in June", "spacing_irrigated": "75\u00d745cm (irrigated) or 90\u00d760cm (rainfed)", "spacing_rainfed": "90\u00d760cm or 120\u00d760cm with intercropping", "depth_cm": "3-5cm", "seed_rate": "2.5-3.5 kg/ha (hybrid/Bt cotton)"}, "irrigation": {"critical_stages": "Germination, flowering, boll development", "irrigations": "4-6 in irrigated regions; rainfed depends on monsoon", "method": "Furrow or drip"}, "fertilization": {"npk_kg_ha": "N150-P60-K60 for irrigated hybrid Bt cotton", "schedule": "Basal: 50%N+100%P+100%K; Top dressing: 25%N at squaring + 25%N at flowering", "boron": "Borax 0.5 kg/ha at flowering (critical for boll set)"}, "pest_management": {"key_pests": ["Cotton Bollworm (Helicoverpa armigera)", "Pink Bollworm (Pectinophora gossypiella)", "Whitefly (Bemisia tabaci)", "Thrips (Thrips tabaci)", "Aphids"], "ipm_strategy": "Pheromone traps; Trichogramma release; Bt Cry1Ac (genetic resistance); NPV spray; monitor weekly", "chemical_rotation": "Rotate Emamectin benzoate / Chlorantraniliprole / Spinosad / Indoxacarb (no repeating same chemistry)"}, "harvesting": {"method": "Repeated hand-pickings (3-4 pickings as bolls open); mechanical picking in USA", "timing": "Pick when boll fully open and lock open for 3-5 days", "yield_kg_ha": "2000-2500 kg/ha seed cotton (lint yield 700-900 kg/ha)"}, "ginning": {"process": "Saw-gin or roller-gin to separate lint from seed", "lint_to_seed": "1 kg lint from 2.7 kg seed cotton (37% outturn)"}}', '2026-06-26 15:48:13'),
    (7, 'Sugarcane', 'Saccharum officinarum and hybrids', 'New Guinea (Pacific Islands)', 'Tropical and subtropical', '27-38°C growing season; 12-20°C for maturation and sucrose accumulation', '1500-2500mm; needs dry period for sucrose accumulation', 'Deep, well-drained alluvial or loamy soil', '6.0-8.0', '', '', '', 'Drip irrigation most efficient; furrow also used', 'Establishment, grand growth period (3-9 months)', '1500-2500mm total', 'N280-P120-K160 planted crop; N240-P80-K140 ratoon', 'Basal: 50%P+50%K; N split every 45 days (5 splits)', '12-14 months for plant crop; 10-12 months for ratoon; CCS (Commercial Cane Sugar) > 10%', 'Manual harvesting (topped and detrashed) or mechanical harvester', '70-100 t/ha cane; 8-11 t/ha sugar', '{"botanical_name": "Saccharum officinarum and hybrids", "origin": "New Guinea (Pacific Islands)", "climate": {"type": "Tropical and subtropical", "temp_optimum_C": "27-38\u00b0C growing season; 12-20\u00b0C for maturation and sucrose accumulation", "rainfall_mm": "1500-2500mm; needs dry period for sucrose accumulation", "altitude_m": "0-1500m"}, "soil": {"type": "Deep, well-drained alluvial or loamy soil", "ph_range": "6.0-8.0", "depth_required_m": "1.0m minimum", "avoid": "Waterlogged, saline, or stony soils"}, "varieties": {"Co_0238": "India \u2014 current dominant variety; high sucrose, high yield", "CoH_56": "Haryana India \u2014 spring plant", "Isoprime": "Pakistan \u2014 high tonnage", "SP_70_1143": "Brazil \u2014 widely adapted"}, "planting": {"method": "Sett planting (3-4 bud sets) or tissue culture plants", "spacing": "90cm rows (irrigated); 120cm rows (rainfed); plant setts 50-60cm apart in furrow", "depth_cm": "10-15cm furrow", "season": "October-November (early spring planting) or February-March (spring)"}, "ratoon_crop": "First ratoon and second ratoon are common (each adds one crop without replanting)", "irrigation": {"critical_stages": "Establishment, grand growth period (3-9 months)", "method": "Drip irrigation most efficient; furrow also used", "water_requirement_mm": "1500-2500mm total", "deficit_period": "Withhold irrigation last 45 days before harvest for sucrose accumulation"}, "fertilization": {"npk_kg_ha": "N280-P120-K160 planted crop; N240-P80-K140 ratoon", "schedule": "Basal: 50%P+50%K; N split every 45 days (5 splits)", "silicon": "Ca silicate 250 kg/ha for stem strength, disease and pest resistance", "zinc": "ZnSO4 25 kg/ha if deficient"}, "harvesting": {"maturity": "12-14 months for plant crop; 10-12 months for ratoon; CCS (Commercial Cane Sugar) > 10%", "testing": "Brix refractometer (reading > 18); sucrose purity > 80%", "method": "Manual harvesting (topped and detrashed) or mechanical harvester", "yield_t_ha": "70-100 t/ha cane; 8-11 t/ha sugar"}, "mill_processing": {"steps": "Crush \u2192 Extract juice \u2192 Clarify \u2192 Evaporate \u2192 Crystallize \u2192 Centrifuge \u2192 Dry sugar", "bagasse": "Used as fuel in mills; also paper and board manufacturing"}}', '2026-06-26 15:48:13'),
    (8, 'Banana', 'Musa spp. (acuminata, balbisiana and hybrids)', 'Southeast Asia (Papua New Guinea region)', 'Humid tropical', '26-30°C; growth stops below 15°C and above 38°C', '2000-2500mm; well distributed throughout year; critical to avoid dry spells', 'Deep, fertile, well-drained loam', '5.5-7.0', '', '', '', 'Drip irrigation (most efficient); micro-sprinkler', 'Flowering and bunch development (6-9 months)', '2000-2500mm total', '', '', '', 'Whole bunch harvested at once by cutting bunch stalk', '40-60 t/ha (good management); 25-35 t/ha normal', '{"botanical_name": "Musa spp. (acuminata, balbisiana and hybrids)", "origin": "Southeast Asia (Papua New Guinea region)", "climate": {"type": "Humid tropical", "temp_optimum_C": "26-30\u00b0C; growth stops below 15\u00b0C and above 38\u00b0C", "rainfall_mm": "2000-2500mm; well distributed throughout year; critical to avoid dry spells", "wind_tolerance": "Susceptible to wind damage; windbreaks recommended", "altitude_m": "0-1500m"}, "soil": {"type": "Deep, fertile, well-drained loam", "ph_range": "5.5-7.0", "depth_required_m": "0.75m", "organic_matter": "High OM preferred", "avoid": "Waterlogged soils (root rot); shallow rocky soils"}, "varieties": {"Cavendish_Robusta": "Main export variety worldwide", "Cavendish_Grand_Naine": "Tissue culture; preferred for high density planting", "Dwarf_Cavendish": "India local market; shorter plant", "Nendran": "Kerala India \u2014 cooking variety; larger fruit", "Red_Banana": "Specialty market; red-purple skin when ripe"}, "planting": {"material": "Tissue culture plants (disease-free, uniform); suckers; corms", "spacing": "2\u00d72m (5000/ha); 1.8\u00d71.5m (high density paired rows)", "pit_size": "60\u00d760\u00d760cm; fill with topsoil + FYM 10kg + lime", "season": "Year-round in tropics; plant before onset of rains"}, "crop_management": {"desuckering": "Allow only 1 sword sucker per plant; remove all other suckers at bi-weekly intervals", "denavelling": "Remove male bud (''navil'') 10-15 days after last hand of bunch emerges", "propping": "Prop plants at 6-7 months when bunch is heavy", "bunch_bagging": "Cover bunch with polythene bag to protect from pests, improve quality"}, "irrigation": {"method": "Drip irrigation (most efficient); micro-sprinkler", "frequency": "Daily in summer (60-80 L/plant/day); 3-4 days in monsoon", "critical_stages": "Flowering and bunch development (6-9 months)", "water_requirement_mm": "2000-2500mm total"}, "fertilization": {"per_plant_year": "N200g + P100g + K300g; in 4-6 splits through fertigation", "organic": "FYM/compost 20 kg per plant at planting", "micronutrients": "ZnSO4, MgSO4 soil or foliar if deficient"}, "harvesting": {"maturity_indices": "125-150 days from bunch emergence; fruit angularity less pronounced (roundness); necks lighten", "method": "Whole bunch harvested at once by cutting bunch stalk", "yield_t_ha": "40-60 t/ha (good management); 25-35 t/ha normal"}, "post_harvest": {"ethylene_ripening": "200-250 ppm ethylene in ripening room 18-22\u00b0C for 24-48 hours for uniform color", "storage": "13-14\u00b0C (below 12\u00b0C causes chilling injury \u2014 skin blackens)", "shelf_life": "7-14 days at 13\u00b0C"}}', '2026-06-26 15:48:13'),
    (9, 'Soybean', 'Glycine max', 'Northern China', 'Warm temperate to tropical', '20-30°C; frost-sensitive', '600-1000mm', 'Well-drained loam to clay loam', '6.0-7.0', '', '80-100 kg/ha', '45×5cm or 30×5cm depending on fertility', '', 'R1 flowering, R5 seed fill (very critical)', '500-700mm', 'N20-P80-K40 (minimal N needed with good Rhizobium inoculation)', '', '90-95% pods golden-brown; moisture < 15%', 'Combine harvester or manual', '1.5-3.0 t/ha', '{"botanical_name": "Glycine max", "origin": "Northern China", "climate": {"type": "Warm temperate to tropical", "temp_optimum_C": "20-30\u00b0C; frost-sensitive", "rainfall_mm": "600-1000mm", "photoperiod": "Short-day plant; flowers as day length shortens in autumn"}, "soil": {"type": "Well-drained loam to clay loam", "ph_range": "6.0-7.0", "special": "Fixes nitrogen via Bradyrhizobium japonicum; inoculation critical for first planting"}, "varieties": {"JS_335": "India \u2014 most popular; 90 days; 2.5 t/ha", "NRC_37": "High protein variety", "Bragg": "USA \u2014 tropical adaptation"}, "rhizobium_inoculation": "Seed inoculation with Bradyrhizobium japonicum is essential; can fix 100-300 kg N/ha", "seed_rate": "80-100 kg/ha", "spacing": "45\u00d75cm or 30\u00d75cm depending on fertility", "irrigation": {"critical_stages": "R1 flowering, R5 seed fill (very critical)", "supplemental": "1-2 irrigations if rainfall insufficient during pod fill", "water_requirement_mm": "500-700mm"}, "fertilization": {"npk_kg_ha": "N20-P80-K40 (minimal N needed with good Rhizobium inoculation)", "starter_N": "20 kg N basal only to support early growth before nodulation"}, "weed_management": {"critical_period": "0-45 days", "herbicides": "Pendimethalin pre-emergence; Imazethapyr 10% SL post-emergence for grasses"}, "harvesting": {"maturity_indicator": "90-95% pods golden-brown; moisture < 15%", "method": "Combine harvester or manual", "yield_t_ha": "1.5-3.0 t/ha"}}', '2026-06-26 15:48:13'),
    (10, 'Chickpea', 'Cicer arietinum', 'Turkey and Middle East', 'Cool dry conditions', '15-25°C; tolerates light frost at vegetative stage', '400-1000mm; sensitive to excess moisture', 'Well-drained sandy loam to clay loam', '6.0-9.0 (wide tolerance)', '', '60-80 kg/ha (desi); 100-120 kg/ha (kabuli)', '', '', '', '', '', '', '100-120 days; plants and pods golden-brown', 'Manual or combine; threshing by power thresher', '1.5-2.5 t/ha', '{"botanical_name": "Cicer arietinum", "origin": "Turkey and Middle East", "climate": {"type": "Cool dry conditions", "temp_optimum_C": "15-25\u00b0C; tolerates light frost at vegetative stage", "rainfall_mm": "400-1000mm; sensitive to excess moisture"}, "soil": {"type": "Well-drained sandy loam to clay loam", "ph_range": "6.0-9.0 (wide tolerance)", "avoid": "Waterlogged soils; salinity"}, "types": {"desi": "Small, dark-seeded; higher protein; most grown in South Asia and Ethiopia", "kabuli": "Large, cream-colored; hummus type; Middle East and Mediterranean markets"}, "varieties": {"JG_11": "India \u2014 short duration (80 days); high yield 2.5 t/ha", "KAK_2": "Kabuli type for export markets", "ICC_4958": "Drought-tolerant; deep-rooted"}, "rhizobium": "Inoculate with Mesorhizobium ciceri for nitrogen fixation", "seed_rate": "60-80 kg/ha (desi); 100-120 kg/ha (kabuli)", "wilt_resistance": "Use wilt-resistant varieties; soil drench with Trichoderma in history-wilt fields", "harvesting": {"maturity": "100-120 days; plants and pods golden-brown", "method": "Manual or combine; threshing by power thresher", "yield_t_ha": "1.5-2.5 t/ha"}}', '2026-06-26 15:48:13'),
    (11, 'Coconut', 'Cocos nucifera', 'Pacific/Southeast Asia (disputed)', 'Humid tropical', '27-32°C; minimum 15°C; no frost tolerance', '1500-2500mm; well-distributed', 'Sandy loam to loamy soils; alluvial soils', '5.5-8.0', '', '', '', 'Drip, basin, or flood', '', '', '', 'Split into 2-3 applications (June, Sept, Dec)', '', '', '', '{"botanical_name": "Cocos nucifera", "origin": "Pacific/Southeast Asia (disputed)", "climate": {"type": "Humid tropical", "temp_optimum_C": "27-32\u00b0C; minimum 15\u00b0C; no frost tolerance", "rainfall_mm": "1500-2500mm; well-distributed", "humidity": "> 80%", "altitude_m": "0-600m"}, "soil": {"type": "Sandy loam to loamy soils; alluvial soils", "ph_range": "5.5-8.0", "depth_required_m": "1.2m", "special": "Tolerates salinity better than most trees; coastal adaptability"}, "varieties": {"Tall": "West Coast Tall (WCT) \u2014 traditional; 10-15m; starts bearing 6-8 years; 60-80 nuts/year", "Dwarf": "Chowghat Orange Dwarf (COD) \u2014 3-5m; bearing at 3-4 years; tenderness; 80-100 nuts/year", "Hybrid": "COD\u00d7WCT Hybrids \u2014 160-200 nuts/year; high copra recovery"}, "planting": {"pit_size": "1\u00d71\u00d71m", "spacing": "7.5\u00d77.5m triangular; or 8\u00d78m square", "seedlings": "9-12 month old transplants from certified nursery", "time": "June-November (monsoon)"}, "irrigation": {"method": "Drip, basin, or flood", "water_requirement": "2200 liters/palm/year (full supplement)", "drip_schedule": "15-20 L/palm/day (summer); 5-10 L/palm/day (monsoon)"}, "fertilization": {"bearing_palm_year": "N500g + P320g + K1200g + Mg100g per palm per year", "schedule": "Split into 2-3 applications (June, Sept, Dec)", "chlorine": "Coconut is chlorine-responsive: NaCl 2 kg/palm/year improves nut yield", "boron": "Borax 50g/palm/year prevents button shedding"}, "intercrops": "Banana, Pineapple, Ginger, Turmeric, Vegetables, Cacao (most common intercrops under coconut)", "harvesting": {"frequency": "Every 30-45 days (harvesting cycle)", "copra": "Dried coconut kernel; harvest at 12 months (full brown coconut)", "tender_coconut": "Harvest at 7-8 months (green/yellow stage; water stage)", "yield_nuts_year": "60-80 (Tall); 160-200 (Hybrid)"}}', '2026-06-26 15:48:13');

DROP TABLE IF EXISTS rag_documents CASCADE;
CREATE TABLE rag_documents (
    id INTEGER PRIMARY KEY NOT NULL,
    document_type VARCHAR(100) NOT NULL,
    title VARCHAR(500) NOT NULL,
    content VARCHAR(255) NOT NULL,
    source_module VARCHAR(100) NULL,
    plant_name VARCHAR(200) NULL,
    tags VARCHAR(500) NULL,
    tfidf_vector VARCHAR(255) NULL,
    created_at TIMESTAMP NULL,
    updated_at TIMESTAMP NULL
);

-- Data for rag_documents (88 rows)
INSERT INTO rag_documents (id, document_type, title, content, source_module, plant_name, tags, tfidf_vector, created_at, updated_at) VALUES
    (1, 'disease', 'Early Blight in Tomato', 'Disease: Early Blight
Pathogen: Alternaria solani
Type: Fungal
Affected Plant: Tomato
Host Range: Tomato, Potato, Eggplant
Symptoms: Small, dark brown circular spots with concentric rings (target board pattern) on older lower leaves. Leaf yellowing, premature leaf drop, dark sunken lesions at stem-ends of fruit, stem collar rot
Treatment: Neem oil (4ml/L + 2ml soap), Copper oxychloride 50% WP (3g/L), Trichoderma harzianum soil drench, Baking soda spray (5g/L). Mancozeb 75% WP (2g/L), Azoxystrobin 23% SC (1ml/L), Chlorothalonil 75% WP (2g/L), Propiconazole 25% EC (1ml/L)
Prevention: Use certified disease-free seeds, crop rotation (3 years), remove infected debris, avoid overhead irrigation, stake plants for air circulation', 'diseases_db', 'Tomato', 'Fungal,Tomato,Alternaria solani', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (2, 'disease', 'Late Blight in Tomato', 'Disease: Late Blight
Pathogen: Phytophthora infestans
Type: Oomycete
Affected Plant: Tomato
Host Range: Tomato, Potato
Symptoms: Water-soaked irregular grayish-green patches on leaves, usually starting from leaf tips and edges. Fuzzy white sporulating lesions on underside of leaves in humid conditions, greasy dark green-black patches on fruit, entire plant collapse with putrid smell
Treatment: Copper hydroxide (3g/L) as protective spray, Bordeaux mixture (1%), maintain dry conditions. Metalaxyl-M + Mancozeb (Ridomil Gold) 2.5g/L, Cymoxanil + Famoxadone 0.5g/L, Dimethomorph 0.5g/L
Prevention: Plant resistant varieties, ensure good drainage, avoid overhead irrigation, scout regularly during cool wet weather, destroy volunteer plants', 'diseases_db', 'Tomato', 'Oomycete,Tomato,Phytophthora infestans', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (3, 'disease', 'Tomato Yellow Leaf Curl Virus (TYLCV) in Tomato', 'Disease: Tomato Yellow Leaf Curl Virus (TYLCV)
Pathogen: Tomato yellow leaf curl virus
Type: Viral
Affected Plant: Tomato
Host Range: Tomato, Pepper, Bean, Eggplant
Symptoms: Upward and inward curling of leaflets, yellowing at leaf margins. Severe stunting, complete yellowing, flower drop, no fruit set or deformed fruits
Treatment: No cure once infected; control whitefly vector with neem oil, yellow sticky traps, reflective mulch. Imidacloprid or Thiamethoxam for whitefly control. Mineral oil sprays to reduce whitefly transmission
Prevention: Plant TYLCV-resistant varieties, use insect-proof netting in nursery, roguing infected plants immediately, control whiteflies', 'diseases_db', 'Tomato', 'Viral,Tomato,Tomato yellow leaf curl virus', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (4, 'disease', 'Fusarium Wilt in Tomato', 'Disease: Fusarium Wilt
Pathogen: Fusarium oxysporum f. sp. lycopersici
Type: Fungal
Affected Plant: Tomato
Host Range: Tomato (host-specific)
Symptoms: Yellowing and wilting of lower leaves starting on one side of the plant, often one branch first. Complete wilting and death, brown internal vascular discoloration visible when stem is cut crosswise
Treatment: Trichoderma harzianum soil treatment, Solarization (clear polyethylene film over moist soil for 4-6 weeks). No effective chemical cure; soil fumigation with Metam sodium before planting as preventive
Prevention: Plant resistant varieties (race-specific), crop rotation (4+ years), avoid wounding roots, soil solarization', 'diseases_db', 'Tomato', 'Fungal,Tomato,Fusarium oxysporum f. sp. lycopersici', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (5, 'disease', 'Bacterial Wilt in Tomato', 'Disease: Bacterial Wilt
Pathogen: Ralstonia solanacearum
Type: Bacterial
Affected Plant: Tomato
Host Range: Tomato, Potato, Pepper, Eggplant, Banana, Tobacco, Ginger
Symptoms: Sudden wilting of top leaves during hottest part of the day, recovery at night. Permanent wilting even at night, water-soaked stem interior, oozing of bacterial slime (white to gray) from cut stems dipped in water
Treatment: No effective cure. Copper-based bactericides as weak suppressants. No effective chemical treatment available
Prevention: Plant resistant varieties, crop rotation (minimum 3 years), soil solarization, avoid waterlogging, remove infected plants and soil, use clean tools', 'diseases_db', 'Tomato', 'Bacterial,Tomato,Ralstonia solanacearum', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (6, 'disease', 'Septoria Leaf Spot in Tomato', 'Disease: Septoria Leaf Spot
Pathogen: Septoria lycopersici
Type: Fungal
Affected Plant: Tomato
Host Range: Tomato, Potato (limited)
Symptoms: Small, circular water-soaked spots on lower leaves with dark brown margins and lighter gray-white centers with tiny black dots (pycnidia). Extensive defoliation starting from bottom of plant upward, sun-scalded fruits exposed to direct sun
Treatment: Copper oxychloride 50% WP (3g/L), neem oil spray, remove infected lower leaves. Chlorothalonil (2g/L), Mancozeb (2g/L), Azoxystrobin (0.5ml/L)
Prevention: Crop rotation, remove infected plant debris, avoid overhead irrigation, stake and prune for air circulation', 'diseases_db', 'Tomato', 'Fungal,Tomato,Septoria lycopersici', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (7, 'disease', 'Powdery Mildew (Tomato) in Tomato', 'Disease: Powdery Mildew (Tomato)
Pathogen: Leveillula taurica
Type: Fungal
Affected Plant: Tomato
Host Range: Tomato, Pepper, Eggplant
Symptoms: Pale yellow spots on upper leaf surface, white powdery growth visible on underside. Entire leaf covered with white powder, premature defoliation
Treatment: Wettable sulfur (3g/L), potassium bicarbonate (5g/L), neem oil, diluted milk (1:9). Hexaconazole (1ml/L), Propiconazole (1ml/L), Tebuconazole (1ml/L)
Prevention: Good air circulation, avoid dense planting, resistant varieties', 'diseases_db', 'Tomato', 'Fungal,Tomato,Leveillula taurica', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (8, 'disease', 'Blossom End Rot in Tomato', 'Disease: Blossom End Rot
Pathogen: Calcium deficiency (Physiological)
Type: Physiological Disorder
Affected Plant: Tomato
Host Range: Tomato, Pepper, Eggplant, Watermelon, Squash
Symptoms: Light brown water-soaked area at blossom end of green fruit. Expanding dark brown to black leathery sunken patch at fruit base, secondary fungal colonization
Treatment: Foliar calcium chloride spray (4g/L), consistent irrigation, mulching, agricultural lime in soil. Calcium nitrate foliar spray (2g/L), drip application of calcium chelate
Prevention: Consistent irrigation schedule, mulch to retain soil moisture, soil pH 6.2-6.8, avoid excess ammonium nitrogen', 'diseases_db', 'Tomato', 'Physiological Disorder,Tomato,Calcium deficiency (Physiological)', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (9, 'disease', 'Root Knot Nematode in Tomato', 'Disease: Root Knot Nematode
Pathogen: Meloidogyne incognita, M. javanica
Type: Nematode
Affected Plant: Tomato
Host Range: Tomato, Pepper, Cucumber, Beans, and 2,000+ other plant species
Symptoms: Wilting during hot hours, poor plant vigor, chlorosis resembling nutrient deficiency. Typical galls (root knots) on roots when pulled, stunted growth, reduced yield
Treatment: Marigold intercropping (Tagetes sp.), neem cake soil application, Paecilomyces lilacinus, Pochonia chlamydosporia. Carbofuran 3G (33kg/ha soil application), Ethoprophos 10G granules, Oxamyl
Prevention: Crop rotation with non-host crops (maize, cereals), soil solarization, use resistant varieties (Mi-gene)', 'diseases_db', 'Tomato', 'Nematode,Tomato,Meloidogyne incognita, M. javanica', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (10, 'disease', 'Rice Blast in Rice', 'Disease: Rice Blast
Pathogen: Pyricularia oryzae (Magnaporthe oryzae)
Type: Fungal
Affected Plant: Rice
Host Range: Rice, Barley, Wheat, Foxtail millet
Symptoms: Spindle-shaped (diamond) lesions on leaves with gray-white center and dark brown to reddish-brown margins. Neck rot: lesion at panicle neck causes the head to break and hang down (Neck Blast). Grain blast: empty chaffy grains. Node blast: dark lesions at stem nodes.
Treatment: Spray Pseudomonas fluorescens (1% w/v), seed treatment with Trichoderma, avoid excess nitrogen. Tricyclazole 75% WP (0.6g/L), Isoprothiolane 40% EC (1.5ml/L), Kasugamycin 3% SL (1.5ml/L), Azoxystrobin
Prevention: Use blast-resistant varieties (BPT 5204, Swarna Sub1), balanced N fertilization, wider spacing for air circulation, destroy stubble', 'diseases_db', 'Rice', 'Fungal,Rice,Pyricularia oryzae (Magnaporthe oryzae)', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (11, 'disease', 'Bacterial Leaf Blight (BLB) in Rice', 'Disease: Bacterial Leaf Blight (BLB)
Pathogen: Xanthomonas oryzae pv. oryzae
Type: Bacterial
Affected Plant: Rice
Host Range: Rice (primary), wild Oryza species
Symptoms: Water-soaked to yellowish stripes along leaf margins, turning white to grayish, ''Kresek'' phase in young seedlings (complete wilting). Milky, opaque bacterial exudate (dried beads) visible in morning on leaf tips, pale yellow ''straw'' leaves, withered diseased panicles
Treatment: Drain fields; copper hydroxide (2g/L) as weak bactericide spray. Streptomycin + Tetracycline combination (limited effectiveness); Copper oxychloride preventively
Prevention: Plant resistant varieties (IR64, Swarna), avoid excessive nitrogen, drain infected fields, destroy stubble', 'diseases_db', 'Rice', 'Bacterial,Rice,Xanthomonas oryzae pv. oryzae', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (12, 'disease', 'Sheath Blight in Rice', 'Disease: Sheath Blight
Pathogen: Rhizoctonia solani AG1-IA
Type: Fungal
Affected Plant: Rice
Host Range: Rice, Maize, Soybean, Sugarcane, and many other crops
Symptoms: Oval to elliptical greenish-gray lesions with white-gray interior and brownish border on leaf sheaths at water level. Lesions coalesce and extend to upper leaves, white mycelial growth and brown sclerotia visible, complete sheath and leaf death
Treatment: Trichoderma harzianum or T. viride soil application (2.5 kg/ha), Pseudomonas fluorescens spray. Hexaconazole 5% EC (1ml/L), Propiconazole 25% EC (1ml/L), Validamycin 3% L (2ml/L), Carbendazim (1g/L)
Prevention: Reduce plant density, lower nitrogen, drain standing water, use resistant varieties', 'diseases_db', 'Rice', 'Fungal,Rice,Rhizoctonia solani AG1-IA', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (13, 'disease', 'Brown Spot in Rice', 'Disease: Brown Spot
Pathogen: Helminthosporium oryzae (Bipolaris oryzae)
Type: Fungal
Affected Plant: Rice
Host Range: Rice, Corn, Sorghum, Sugarcane
Symptoms: Small, oval to circular spots on leaves with yellow halo; dark brown margins and lighter centers. Spots enlarge to typical oval brown spots, leaves yellow and die; glume discoloration leading to pecky rice
Treatment: Trichoderma seed treatment, adequate potassium nutrition. Mancozeb 75% WP (2g/L), Propiconazole 25% EC (1ml/L), Iprodione (1.5g/L)
Prevention: Treat seeds with fungicide, correct soil nutrition (especially K and Si), use certified seeds, crop rotation', 'diseases_db', 'Rice', 'Fungal,Rice,Helminthosporium oryzae (Bipolaris oryzae)', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (14, 'disease', 'False Smut in Rice', 'Disease: False Smut
Pathogen: Ustilaginoidea virens
Type: Fungal
Affected Plant: Rice
Host Range: Rice
Symptoms: Individual spikelets converted to small velvet-like greenish balls. Balls enlarge to 10mm diameter, becoming orange-yellow then olive-green with black powdery spores, scattered through panicle
Treatment: Propiconazole-based sprays at booting stage. Propiconazole 25% EC (1ml/L) or Azoxystrobin at booting stage
Prevention: Spray preventive fungicide at booting stage, avoid late planting, balanced nutrition', 'diseases_db', 'Rice', 'Fungal,Rice,Ustilaginoidea virens', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (15, 'disease', 'Stripe Rust (Yellow Rust) in Wheat', 'Disease: Stripe Rust (Yellow Rust)
Pathogen: Puccinia striiformis f. sp. tritici
Type: Fungal
Affected Plant: Wheat
Host Range: Wheat, Barley, Triticale, wild grasses
Symptoms: Stripe of yellow-orange uredia arranged in rows along leaf veins on upper leaf surface. Extensive yellowing of leaves, black teliospores in stripes, reduced grain fill, shriveled kernels
Treatment: Wettable sulfur preventively; no effective organic cure. Propiconazole 25% EC (1ml/L), Tebuconazole 250 EW (1ml/L), Azoxystrobin + Propiconazole
Prevention: Plant resistant varieties (HD-3226, WH1105), timely sowing to escape high-risk period, prophylactic fungicide at flag leaf stage', 'diseases_db', 'Wheat', 'Fungal,Wheat,Puccinia striiformis f. sp. tritici', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (16, 'disease', 'Stem Rust (Black Rust) in Wheat', 'Disease: Stem Rust (Black Rust)
Pathogen: Puccinia graminis f. sp. tritici
Type: Fungal
Affected Plant: Wheat
Host Range: Wheat, Barley, Rye, many grasses
Symptoms: Brick-red oval to elongated blisters (pustules) on stems and leaves that rupture releasing reddish-brown powdery spores. Black teliospore pustules in late season, lodging of stems, shriveled grain
Treatment: Wettable sulfur; remove barberry bushes from fields. Propiconazole 25% EC (1ml/L), Tebuconazole (1ml/L), at first sign of infection
Prevention: Rust-resistant varieties, eradicate barberry, prophylactic fungicide in Ug99-risk areas', 'diseases_db', 'Wheat', 'Fungal,Wheat,Puccinia graminis f. sp. tritici', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (17, 'disease', 'Loose Smut in Wheat', 'Disease: Loose Smut
Pathogen: Ustilago tritici
Type: Fungal
Affected Plant: Wheat
Host Range: Wheat
Symptoms: Diseased plants emerge earlier; infected ear with black spore mass instead of grain. Complete head replaced by black teliospore mass that disperses, leaving bare rachis
Treatment: Hot water seed treatment (52°C for 10 minutes). Carboxin + Thiram seed treatment (2g/kg seed), Tebuconazole seed treatment
Prevention: Use certified smut-free seeds, systemic seed treatment fungicides, plant resistant varieties', 'diseases_db', 'Wheat', 'Fungal,Wheat,Ustilago tritici', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (18, 'disease', 'Powdery Mildew (Wheat) in Wheat', 'Disease: Powdery Mildew (Wheat)
Pathogen: Blumeria graminis f. sp. tritici
Type: Fungal
Affected Plant: Wheat
Host Range: Wheat (host-specific)
Symptoms: White fluffy powdery patches on upper leaf surface of lower leaves. White-gray coating on all green parts, yellowing and drying of leaves, cleistothecia (black dots) visible in old patches
Treatment: Wettable sulfur (3g/L), potassium bicarbonate. Propiconazole 25% EC (1ml/L), Triadimefon 25% WP (1g/L), Azoxystrobin
Prevention: Resistant varieties, avoid dense planting, balanced nitrogen, timely fungicide sprays', 'diseases_db', 'Wheat', 'Fungal,Wheat,Blumeria graminis f. sp. tritici', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (19, 'disease', 'Northern Corn Leaf Blight (NCLB) in Maize', 'Disease: Northern Corn Leaf Blight (NCLB)
Pathogen: Exserohilum turcicum (Setosphaeria turcica)
Type: Fungal
Affected Plant: Maize
Host Range: Maize, Sorghum, Sudan grass
Symptoms: Long (5-15cm) elliptical tan to grayish-green lesions with wavy margins on lower leaves. Extensive leaf blighting from bottom of plant upward, dark olive-green spore mass on lesions in humid conditions
Treatment: Copper-based fungicides preventively. Azoxystrobin + Propiconazole (Quilt Xcel 1L/ha), Propiconazole alone (1ml/L)
Prevention: Resistant hybrids, crop rotation, remove infected debris, timely planting', 'diseases_db', 'Maize', 'Fungal,Maize,Exserohilum turcicum (Setosphaeria turcica)', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (20, 'disease', 'Maize Lethal Necrosis (MLN) in Maize', 'Disease: Maize Lethal Necrosis (MLN)
Pathogen: Maize chlorotic mottle virus (MCMV) + Potyviruses
Type: Viral
Affected Plant: Maize
Host Range: Maize, Sorghum, some grasses
Symptoms: Chlorotic (yellow) streaks and mottling on younger leaves; pale green to yellow leaf discoloration. Complete necrosis of all leaves from leaf tip, brown papery leaves, ear rot, premature death
Treatment: No cure; control insect vectors with neem oil, reflective mulch. No direct treatment; insecticides for vector control (Imidacloprid, Thiamethoxam)
Prevention: Plant MLN-tolerant/resistant varieties, control thrips and aphids, crop rotation, early planting, remove infected plants', 'diseases_db', 'Maize', 'Viral,Maize,Maize chlorotic mottle virus (MCMV) + Potyviruses', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (21, 'disease', 'Gray Leaf Spot in Maize', 'Disease: Gray Leaf Spot
Pathogen: Cercospora zeae-maydis
Type: Fungal
Affected Plant: Maize
Host Range: Maize
Symptoms: Small, irregular tan spots with yellow halos, mainly on lower leaves. Elongated, rectangular, grayish-tan lesions limited by leaf veins, covering entire leaf
Treatment: Copper-based sprays preventively. Azoxystrobin, Propiconazole, Pyraclostrobin at tasseling stage
Prevention: Hybrid resistance, crop rotation, tillage to bury debris, fungicide at VT/R1', 'diseases_db', 'Maize', 'Fungal,Maize,Cercospora zeae-maydis', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (22, 'disease', 'Late Blight (Potato) in Potato', 'Disease: Late Blight (Potato)
Pathogen: Phytophthora infestans
Type: Oomycete
Affected Plant: Potato
Host Range: Potato, Tomato
Symptoms: Water-soaked pale green spots on leaves, white sporulation on underside in humid conditions. Dark brown-black lesions on leaves, brown rots on stems, rapid spread of entire field collapse, tuber rot (brown-red internal)
Treatment: Copper hydroxide (2.5-3g/L) preventively, Bordeaux mixture, avoid excessive irrigation. Metalaxyl-M + Mancozeb 2.5g/L, Dimethomorph + Mancozeb, Cymoxanil + Famoxadone, Fluopicolide
Prevention: Plant resistant varieties (Kufri Bahar, Jyoti), use certified disease-free seed tubers, apply fungicide before first rains, destroy volunteer plants', 'diseases_db', 'Potato', 'Oomycete,Potato,Phytophthora infestans', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (23, 'disease', 'Common Scab in Potato', 'Disease: Common Scab
Pathogen: Streptomyces scabies
Type: Bacterial (Actinomycete)
Affected Plant: Potato
Host Range: Potato, Beet, Radish, Carrot
Symptoms: No visible early symptoms on foliage. Brown corky scab lesions (raised, sunken, or russeted) on tuber surface; external quality defect only
Treatment: Soil acidification (sulfur), crop rotation, adequate irrigation during tuber formation. Quintozene PCNB seed treatment (limited), Flutolanil seed treatment
Prevention: Lower soil pH to 5.0-5.5, maintain soil moisture during tuber initiation, rotate with non-susceptible crops (cereals), use scab-resistant varieties', 'diseases_db', 'Potato', 'Bacterial (Actinomycete),Potato,Streptomyces scabies', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (24, 'disease', 'Anthracnose in Mango', 'Disease: Anthracnose
Pathogen: Colletotrichum gloeosporioides
Type: Fungal
Affected Plant: Mango
Host Range: Mango, Papaya, Avocado, many tropical fruits
Symptoms: Dark brown to black spots on young leaves, flowers, and immature fruits; ''blossom blight'' killing flower clusters. Sunken, dark brown lesions on mature fruits that expand rapidly post-harvest; fruit rot; complete flower destruction
Treatment: Copper oxychloride 3g/L, neem oil + copper, hot water dip 52°C for 5 minutes (post-harvest). Carbendazim 0.1% + Mancozeb 0.25% spray, Azoxystrobin + Difenoconazole, Propiconazole 0.1%
Prevention: Prune dead wood, copper spray before flowering, proper post-harvest handling (hot water), waxing, cold chain', 'diseases_db', 'Mango', 'Fungal,Mango,Colletotrichum gloeosporioides', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (25, 'disease', 'Powdery Mildew (Mango) in Mango', 'Disease: Powdery Mildew (Mango)
Pathogen: Oidium mangiferae
Type: Fungal
Affected Plant: Mango
Host Range: Mango
Symptoms: White powdery coating on young leaves, flower clusters, and young fruits. Complete whitening of panicles, flower drop, young fruit drop, malformed surviving fruits
Treatment: Wettable sulfur 3g/L at bud break; diluted milk spray (1:5); potassium bicarbonate. Triadimefon 25% WP (1g/L), Hexaconazole 5% EC (2ml/L), Propiconazole 25% EC (1ml/L), Myclobutanil
Prevention: First spray at bud emergence, second at fruit set; avoid overhead irrigation; morning sprays', 'diseases_db', 'Mango', 'Fungal,Mango,Oidium mangiferae', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (26, 'disease', 'Mango Malformation Disease (MMD) in Mango', 'Disease: Mango Malformation Disease (MMD)
Pathogen: Fusarium mangiferae
Type: Fungal
Affected Plant: Mango
Host Range: Mango
Symptoms: Vegetative malformation: bunchy top appearance with compacted proliferation of shoots (''mango witches'' broom''). Floral malformation: panicle conversion to compact, sterile, green vegetative structure; no fruits formed
Treatment: Remove and burn malformed parts; control mites with acaricides. NAA (Naphthaleneacetic acid) 200ppm spray + Carbendazim (0.1%) at panicle emergence
Prevention: Use disease-free planting material, certified nursery plants, deinfest cutting tools, control mite vectors', 'diseases_db', 'Mango', 'Fungal,Mango,Fusarium mangiferae', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (27, 'disease', 'Panama Wilt (Fusarium Wilt of Banana) in Banana', 'Disease: Panama Wilt (Fusarium Wilt of Banana)
Pathogen: Fusarium oxysporum f. sp. cubense (TR4)
Type: Fungal
Affected Plant: Banana
Host Range: Banana, Plantain
Symptoms: Yellowing of older outer leaves, leaf collapse, starting from leaf margins; brown streaking in pseudostem when cut. Complete plant collapse, pseudostem brown-red internal discoloration from base upward, no fruit production
Treatment: No cure. Soil solarization, biological soil amendments (Trichoderma, compost). No effective chemical treatment
Prevention: Strict quarantine, plant resistant varieties (GCTCV-218 for TR4), clean tools with bleach, avoid infected soil movement', 'diseases_db', 'Banana', 'Fungal,Banana,Fusarium oxysporum f. sp. cubense (TR4)', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (28, 'disease', 'Black Sigatoka (Black Leaf Streak) in Banana', 'Disease: Black Sigatoka (Black Leaf Streak)
Pathogen: Pseudocercospora fijiensis
Type: Fungal
Affected Plant: Banana
Host Range: Banana, Plantain
Symptoms: Tiny pale yellow flecks on lower leaf surface that elongate into brown streaks. Brown-black elongated lesions with yellow halo on upper leaf surface; premature defoliation; green fruit ripening prematurely
Treatment: Copper oxychloride (2-3g/L) sprays, oil-based copper formulations; remove infected leaves. Systemic fungicides on rotation: Propiconazole, Tebuconazole, Fenbuconazole, Chlorothalonil; resistance management essential
Prevention: Resistant varieties, remove lower infected leaves (deleafing), reduce humidity with good drainage and canopy management', 'diseases_db', 'Banana', 'Fungal,Banana,Pseudocercospora fijiensis', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (29, 'disease', 'Cotton Leaf Curl Virus Disease (CLCuD) in Cotton', 'Disease: Cotton Leaf Curl Virus Disease (CLCuD)
Pathogen: Cotton leaf curl Multan virus (CLCuMV) + betasatellite
Type: Viral
Affected Plant: Cotton
Host Range: Cotton, Okra, Hibiscus, Tomato
Symptoms: Upward curling of leaves, vein thickening, enations (leaf-like outgrowths) on underside of leaves. Severe stunting, dark green thickened curled leaves, no boll formation, plant death
Treatment: Control whiteflies with neem extract, reflective mulch, remove infected plants. Imidacloprid/Thiamethoxam soil application for whitefly control; Acetamiprid foliar spray
Prevention: Resistant varieties (NIAB 846, CIM-499), control whiteflies strictly, remove infected plants, use insect-proof nets in nursery', 'diseases_db', 'Cotton', 'Viral,Cotton,Cotton leaf curl Multan virus (CLCuMV) + betasatellite', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (30, 'disease', 'Damping Off in General', 'Disease: Damping Off
Pathogen: Pythium spp., Rhizoctonia solani, Fusarium spp.
Type: Fungal / Oomycete
Affected Plant: General
Host Range: All vegetable and field crops in seedling stage
Symptoms: Seeds fail to germinate (pre-emergence damping off), or seedlings collapse just below soil level (post-emergence). Water-soaked ''pinched'' stem at soil level, seedling falls over, dark discoloration at base
Treatment: Chilled neem cake in soil, well-drained media, Trichoderma seed treatment, chamomile tea drench. Metalaxyl 35% DS seed treatment, Captan 50% WP seed treatment (2g/kg), copper sulfate soil drench
Prevention: Use sterile nursery media, avoid overwatering, thin seedlings, use well-drained trays, treat seeds before sowing', 'diseases_db', 'General', 'Fungal / Oomycete,General,Pythium spp., Rhizoctonia solani, Fusarium spp.', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (31, 'disease', 'Crown Gall in General', 'Disease: Crown Gall
Pathogen: Agrobacterium tumefaciens (Rhizobium radiobacter)
Type: Bacterial
Affected Plant: General
Host Range: Rose, Fruit trees (apple, cherry, walnut), Grapes, more than 600 species
Symptoms: Small, soft, round galls develop at crown (soil line) or on roots. Galls enlarge to large rough, brown, corky tumors; reduced plant vigor, stunting, increased susceptibility to other diseases
Treatment: Cut out galls; treat with Agrobacterium radiobacter strain K-84 (biocontrol) at planting. No effective post-infection treatment; copper bactericides preventively
Prevention: Avoid wounding, use K-84 dip on roots before planting, plant only certified gall-free material', 'diseases_db', 'General', 'Bacterial,General,Agrobacterium tumefaciens (Rhizobium radiobacter)', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (32, 'disease', 'Botrytis Gray Mold in General', 'Disease: Botrytis Gray Mold
Pathogen: Botrytis cinerea
Type: Fungal
Affected Plant: General
Host Range: > 1000 plant species including grapes, strawberry, rose, tomato, lettuce, onion
Symptoms: Water-soaked, brown lesions on petals, leaves, and stems; soft rot. Characteristic gray fluffy fungal sporulation covering lesions; blight of flowers, stem cankers, fruit rot ("ghost spot" on tomato)
Treatment: Remove infected tissue, improve air circulation, reduce humidity; Bacillus subtilis, Trichoderma spray. Iprodione (1.5g/L), Pyrimethanil (1ml/L), Fenhexamid (1g/L), Cyprodinil (0.5g/L). Rotate fungicides for resistance management.
Prevention: Improve air circulation, avoid wounding, remove dead tissue, avoid waterlogging, maintain low humidity', 'diseases_db', 'General', 'Fungal,General,Botrytis cinerea', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (33, 'disease', 'Sclerotinia Stem Rot (White Mold) in General', 'Disease: Sclerotinia Stem Rot (White Mold)
Pathogen: Sclerotinia sclerotiorum
Type: Fungal
Affected Plant: General
Host Range: > 400 species: Canola, Soybean, Sunflower, Bean, Carrot, Celery
Symptoms: Water-soaked lesions on lower stems and branches; bleached, straw-colored stem tissue. White cottony mycelial growth inside and outside infected tissue, large hard black sclerotia (2-10mm) inside stem
Treatment: Thiram-treated seeds, adequate plant spacing, crop rotation. Thiophanate-methyl (1g/L), Boscalid (0.5g/L), Iprodione, Fluazinam at early flowering
Prevention: Crop rotation (non-host crops for 3+ years), avoid dense planting, improve drainage', 'diseases_db', 'General', 'Fungal,General,Sclerotinia sclerotiorum', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (34, 'pest', 'Whitefly - Sucking_Pests', 'Pest: Whitefly (Bemisia tabaci)
Category: Sucking_Pests
Host Plants: Tomato, Cotton, Pepper, Cucumber, Cassava, Sweet Potato, Bean
Damage: Yellowing leaves, sticky honeydew, sooty mold (secondary), vector of 200+ plant viruses (TYLCV, CLCuD, CBSD, cassava mosaic)
Identification: Tiny (1-1.5mm) white-winged insects; fly in clouds when disturbed; yellowish oval nymphs on leaf underside
Organic Control: Yellow sticky traps, neem oil + soap spray (5ml+2ml per L), reflective mulch, soap water spray, Beauveria bassiana
Chemical Control: Imidacloprid 17.8% SL (0.5ml/L), Thiamethoxam 25% WG (0.2g/L), Acetamiprid 20% SP (0.2g/L), Spiromesifen (resistance management)
Biological Control: Encarsia formosa (parasitic wasp), Eretmocerus mundus, Macrolophus pygmaeus (predatory bug), Beauveria bassiana
IPM Notes: Rotate between chemical classes to manage resistance; use systemic at transplanting, contact at adult stage; banker plant system in greenhouses', 'pests_db', 'Tomato, Cotton, Pepper, Cucumber, Cassava, Sweet Potato, Bean', 'Sucking_Pests,Bemisia tabaci', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (35, 'pest', 'Aphids - Sucking_Pests', 'Pest: Aphids (Myzus persicae (Green Peach Aphid); multiple species)
Category: Sucking_Pests
Host Plants: Universal — thousands of plant species (vegetables, fruits, ornamentals, cereals)
Damage: Leaf curling, distortion, yellowing; sticky honeydew with black sooty mold; severe infestations stunt plants; vectors of 200+ plant viruses (CMV, PVY, BYDV)
Identification: Soft-bodied 1-3mm insects, green/yellow/black/pink depending on species; winged and wingless forms; two cornicles (tail tubes) on abdomen
Organic Control: Strong water spray to dislodge; insecticidal soap (1%); neem oil (3-5ml/L); garlic-pepper spray; encourage natural enemies
Chemical Control: Imidacloprid 17.8% SL (0.3ml/L), Dimethoate 30% EC (2ml/L), Flonicamid, Pymetrozine, Spirotetramat
Biological Control: Coccinella septempunctata (ladybug), Chrysoperla carnea (lacewing), Aphidius colemani and A. ervi (parasitic wasps), Syrphid fly larvae
IPM Notes: Banker plant systems (cereal aphid + parasitoid) used in greenhouses; avoid broad-spectrum insecticides that kill natural enemies', 'pests_db', 'Universal — thousands of plant species (vegetables, fruits, ornamentals, cereals)', 'Sucking_Pests,Myzus persicae (Green Peach Aphid); multiple species', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (36, 'pest', 'Thrips - Sucking_Pests', 'Pest: Thrips (Thrips palmi (Melon Thrips); Frankliniella occidentalis (Western Flower Thrips))
Category: Sucking_Pests
Host Plants: Virtually all vegetables, ornamentals, fruits, cotton, onion, cereal crops
Damage: Silvery streaks/scarring on leaves and fruits (from feeding); distorted growth; ''ghost spots'' on petals; TSWV virus symptoms (wilting, bronzing, ring spots)
Identification: Very small (0.5-1.5mm); slender, fringed wings; yellow to dark brown depending on species; move fast
Organic Control: Blue sticky traps (most attractive to thrips), spinosad spray, neem oil, kaolin clay, predatory mites (Neoseiulus cucumeris)
Chemical Control: Spinosad 45% SC (0.3ml/L), Imidacloprid, Abamectin 1.9% EC (0.5ml/L), Cyantraniliprole, Tolfenpyrad
Biological Control: Neoseiulus cucumeris, Amblyseius swirskii (predatory mites); Orius insidiosus (pirate bug); Steinernema feltiae (entomopathogenic nematode) for soil pupae
IPM Notes: Hard to control due to hidden feeding in flowers and leaf tissue; soil pupae require soil drenches; rotate chemical classes', 'pests_db', 'Virtually all vegetables, ornamentals, fruits, cotton, onion, cereal crops', 'Sucking_Pests,Thrips palmi (Melon Thrips); Frankliniella occidentalis (Western Flower Thrips)', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (37, 'pest', 'Spider Mite (Two-Spotted) - Sucking_Pests', 'Pest: Spider Mite (Two-Spotted) (Tetranychus urticae)
Category: Sucking_Pests
Host Plants: Over 1,100 plant species: all vegetables, ornamentals, fruits, cotton, soybean
Damage: Stippled (tiny pale dots/punctures) on leaves from below; leaves turn bronze/yellow and dry; fine silk webbing; premature defoliation
Identification: Tiny (< 0.5mm); two dark spots on pale greenish-yellow body; spin fine silk webbing on leaf underside; visible under hand lens
Organic Control: Water spray to wash off; neem oil 5ml/L; wettable sulfur 3g/L; insecticidal soap; predatory mites release; soap solution sprays
Chemical Control: Abamectin 1.9% EC (0.5ml/L), Spiromesifen 22.9% SC (1ml/L), Hexythiazox 5% EC (1ml/L), Bifenazate, Clofentezine, Fenpyroximate
Biological Control: Phytoseiulus persimilis (excellent predator), Amblyseius californicus, Neoseiulus californicus, Feltiella acarisuga (gall midge)
IPM Notes: Rotate acaricides by chemical class; preserve natural enemies; increase irrigation in dry weather to reduce mite-favorable conditions; do NOT use broad-spectrum insecticides that kill predatory mites', 'pests_db', 'Over 1,100 plant species: all vegetables, ornamentals, fruits, cotton, soybean', 'Sucking_Pests,Tetranychus urticae', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (38, 'pest', 'Mealybugs - Sucking_Pests', 'Pest: Mealybugs (Phenacoccus solenopsis (Cotton Mealybug); Planococcus citri (Citrus Mealybug))
Category: Sucking_Pests
Host Plants: Cotton, Grapes, Citrus, Mango, Cassava, ornamentals, vegetables
Damage: Yellowing, leaf drop, honeydew + sooty mold; cotton twisting; mango malformation spread; overall plant decline and death in severe infestations
Identification: Soft, oval, covered with white mealy wax; pink body visible through wax; waxy filaments around body; colonies in leaf axils and stem crevices
Organic Control: Neem oil + soap spray; rubbing alcohol on cotton swabs; strong water spray; remove waxy coating first; Cryptolaemus montrouzieri release
Chemical Control: Imidacloprid soil drench (2ml/L), Buprofezin 25% WP (1g/L), Chlorpyrifos 20% EC (2.5ml/L), Acetamiprid + Chlorpyrifos
Biological Control: Cryptolaemus montrouzieri (mealybug destroyer beetle), Leptomastix dactylopii (parasitoid wasp), Anagyrus kamali, Acerophagus papayae
IPM Notes: Control ants (which protect mealybugs from predators); reach under waxy coating with oil-based sprays; ant management improves biocontrol effectiveness', 'pests_db', 'Cotton, Grapes, Citrus, Mango, Cassava, ornamentals, vegetables', 'Sucking_Pests,Phenacoccus solenopsis (Cotton Mealybug); Planococcus citri (Citrus Mealybug)', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (39, 'pest', 'Scale Insects - Sucking_Pests', 'Pest: Scale Insects (Diaspidiotus perniciosus (San Jose Scale); Saissetia oleae (Olive Scale))
Category: Sucking_Pests
Host Plants: Fruit trees (apple, pear, citrus, mango), olives, ornamentals
Damage: Yellowing, twig and branch death, reduced fruit quality, bark encrustation; honeydew (soft scales) leading to sooty mold
Identification: Round to oyster-shaped waxy armor covering body; armored scales (Diaspididae) - armor separable from body; soft scales (Coccidae) - armor inseparable
Organic Control: Dormant oil spray (petroleum oil 3-5%) at crawler stage; white summer oil (1-2%); brush off with stiff brush
Chemical Control: Buprofezin (at crawler stage), Chlorpyrifos + oil, Spirotetramat systemic; dormant oil during winter
Biological Control: Encarsia perniciosi (parasitoid of San Jose scale), Comperiella bifasciata, Aphytis melinus (red scale parasitoid)
IPM Notes: Timing at crawler stage is critical; inspect bark regularly; monitor with sticky tape to detect crawlers', 'pests_db', 'Fruit trees (apple, pear, citrus, mango), olives, ornamentals', 'Sucking_Pests,Diaspidiotus perniciosus (San Jose Scale); Saissetia oleae (Olive Scale)', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (40, 'pest', 'Leafhoppers - Sucking_Pests', 'Pest: Leafhoppers (Amrasca biguttula biguttula (Cotton/Okra Leafhopper); Empoasca spp.)
Category: Sucking_Pests
Host Plants: Cotton, Okra, Brinjal, Potato, Grape, Legumes
Damage: Cotton: ''Cotton leaf curl'' or ''Jassid damage'' — leaf edge curling upward, reddening; Potato/Brinjal: leaf hopper burn (hopperburn) — marginal leaf scorch and curling
Identification: Wedge-shaped, 3-4mm; green/yellow; jump sideways when disturbed; run diagonally on plants
Organic Control: Neem seed kernel extract 5%, neem oil; yellow sticky traps; Beauveria bassiana spray
Chemical Control: Imidacloprid 17.8% SL (0.3ml/L), Lambda-cyhalothrin 5% EC (1ml/L), Thiamethoxam, Dimethoate 30% EC (2ml/L)
Biological Control: Anagrus atomus (egg parasitoid in grapes), Gonatocerus ashmeadi, Stethorus ladybugs
IPM Notes: Spray lower leaf surface; morning sprays most effective; hairy-leaved cultivars are less susceptible', 'pests_db', 'Cotton, Okra, Brinjal, Potato, Grape, Legumes', 'Sucking_Pests,Amrasca biguttula biguttula (Cotton/Okra Leafhopper); Empoasca spp.', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (41, 'pest', 'Diamondback Moth - Chewing_Caterpillars', 'Pest: Diamondback Moth (Plutella xylostella)
Category: Chewing_Caterpillars
Host Plants: Cabbage, Cauliflower, Broccoli, Kale, Mustard, Turnip — all Brassica crops
Damage: Windowing: larvae eat leaf tissue from below, leaving translucent papery epidermis on upper surface; total leaf skeletonization in heavy infestations; head borer
Identification: Adult: 8mm, gray-brown moth with diamond pattern on back when wings folded; Larva: pale green, 10mm, wriggle violently when disturbed, dangle from silk thread
Organic Control: Bacillus thuringiensis subsp. kurstaki (Bt-k) spray (most effective); neem seed kernel extract 5%; hand picking; pheromone traps for monitoring
Chemical Control: Spinosad 45% SC (0.3ml/L), Indoxacarb 14.5% SC (1ml/L), Chlorfluazuron (IGR), Emamectin benzoate 5% SG (0.2g/L), Flubendiamide
Biological Control: Cotesia plutellae (parasitic wasp), Diadegma semiclausum, Diadromus collaris; Bacillus thuringiensis
IPM Notes: World''s most insecticide-resistant insect pest. Resistance management is critical. Rotate between Bt, spinosad, indoxacarb, and diamide insecticides.', 'pests_db', 'Cabbage, Cauliflower, Broccoli, Kale, Mustard, Turnip — all Brassica crops', 'Chewing_Caterpillars,Plutella xylostella', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (42, 'pest', 'Fall Armyworm - Chewing_Caterpillars', 'Pest: Fall Armyworm (Spodoptera frugiperda)
Category: Chewing_Caterpillars
Host Plants: Maize (primary), Sorghum, Rice, Sugarcane, Cotton, Tomato, 350+ plant species
Damage: Ragged windows in leaves; characteristic ''shot hole'' damage in whorl; frass in leaf whorl; direct ear damage (in maize); can completely defoliate young plants
Identification: Adult: 38mm wingspan, mottled gray-brown moths; Larva: greenish to brown, inverted ''Y'' mark on head, 4 square black dots on 8th abdominal segment, up to 40mm
Organic Control: Bt-kurstaki or Bt-aizawai spray; fall armyworm pheromone traps; sand+soil in whorl (suffocates larvae); egg mass and larvae hand collection
Chemical Control: Emamectin benzoate 5% SG (0.4g/L into whorl), Chlorantraniliprole (Coragen), Spinetoram, Lambda-cyhalothrin (adult moths)
Biological Control: Telenomus remus (egg parasitoid), Cotesia icipe, Coccygomimus turionellae, Metarhizium rileyi, NPV (Nuclear Polyhedrosis Virus)
IPM Notes: Scouting critical: check whorls for frass and larvae early. Early stage intervention most effective. Avoid broad-spectrum insecticides to preserve natural enemies.', 'pests_db', 'Maize (primary), Sorghum, Rice, Sugarcane, Cotton, Tomato, 350+ plant species', 'Chewing_Caterpillars,Spodoptera frugiperda', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (43, 'pest', 'Cotton Bollworm (Helicoverpa) - Chewing_Caterpillars', 'Pest: Cotton Bollworm (Helicoverpa) (Helicoverpa armigera)
Category: Chewing_Caterpillars
Host Plants: Cotton, Chickpea, Tomato, Maize, Pigeonpea, Sorghum — polyphagous pest of 200+ species
Damage: Entry holes in cotton bolls (with frass-filled tunnels), tomato fruit damage, chickpea pod damage with grain loss, maize kernel damage
Identification: Adult: 35-40mm wingspan, yellowish-brown with dark spot; Larva: variable color (green/brown/pinkish), microspines on body, up to 40mm
Organic Control: NPV spray (2×10¹² POB/ha); HaNPV + cotton Bt; pheromone traps (1/ha); neem seed kernel extract; Bt-k spray
Chemical Control: Emamectin benzoate 5% SG (0.4g/L), Chlorantraniliprole 18.5% SC (0.3ml/L), Indoxacarb, Flubendiamide, Thiodicarb
Biological Control: Trichogramma chilonis (egg parasitoid, 1 lakh/ha weekly), Habrobracon hebetor, Chrysoperla carnea, HaNPV
IPM Notes: Bt crops (Bt cotton, Bt chickpea) used widely; pyrethroid resistance widespread; refuge strategy essential with Bt crops; pheromone trap-based monitoring', 'pests_db', 'Cotton, Chickpea, Tomato, Maize, Pigeonpea, Sorghum — polyphagous pest of 200+ species', 'Chewing_Caterpillars,Helicoverpa armigera', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (44, 'pest', 'Yellow Stem Borer (Rice) - Chewing_Caterpillars', 'Pest: Yellow Stem Borer (Rice) (Scirpophaga incertulas)
Category: Chewing_Caterpillars
Host Plants: Rice (primary), Sugarcane, Wild grasses
Damage: Deadheart: young plants central leaf whorl dies and turns brown (easy to pull out) — vegetative stage; Whitehead: panicle turns white and empty — reproductive stage
Identification: Adult: white moth, 25-30mm wingspan; female has black spot; Larva: creamy white, dark head, up to 20mm
Organic Control: Clip leaf tips of transplanted seedlings (removes egg masses); light traps; pheromone traps; release Trichogramma japonicum
Chemical Control: Cartap hydrochloride 4G granules (25 kg/ha in standing water), Chlorpyrifos 20% EC (2ml/L), Carbofuran 3G, Fipronil 0.3G
Biological Control: Trichogramma japonicum (egg parasitoid, 1 lakh/ha at 10-day intervals), Tetrastichus schoenobii, Telenomus rowani
IPM Notes: Clipping transplant seedlings to remove egg masses is highly effective low-cost management; light traps help reduce adult populations; timing of Trichogramma release is key', 'pests_db', 'Rice (primary), Sugarcane, Wild grasses', 'Chewing_Caterpillars,Scirpophaga incertulas', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (45, 'pest', 'Fruit Fly (Oriental) - Fruit_Pests', 'Pest: Fruit Fly (Oriental) (Bactrocera dorsalis)
Category: Fruit_Pests
Host Plants: Mango, Guava, Banana, Papaya, Star Fruit, Citrus — 150+ fruit species
Damage: Pin-hole entry with sap/gum oozing; fruit surface discoloration, premature fruit drop; soft rotting interior with white maggots; secondary bacterial and fungal infections
Identification: Adult: 8mm, yellowish with dark dorsal stripes; distinctive pointed ovipositor in females; red-brown eyes; Larvae: white maggots inside fruit
Organic Control: Male attractant traps (Methyl eugenol + malathion or GF-120); fruit bagging with paper or plastic bags; Protein bait sprays; pick and destroy infested fallen fruit
Chemical Control: Protein bait spray (GF-120 bait + Spinosad); Cover sprays Malathion 50% EC (2ml/L), Dimethoate (2ml/L); only during non-harvest period
Biological Control: Fopius arisanus (egg-larval parasitoid), Diachasmimorpha longicaudata, Fopius vandenboschi, mass rearing and release of sterile males (SIT)
IPM Notes: Bactrocera dorsalis is a major quarantine pest affecting trade. Use of Methyl eugenol + insecticide traps for mass trapping is most effective. Combination: MAT traps + fruit bagging + protein bait + biocontrol', 'pests_db', 'Mango, Guava, Banana, Papaya, Star Fruit, Citrus — 150+ fruit species', 'Fruit_Pests,Bactrocera dorsalis', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (46, 'pest', 'Mango Stone Weevil - Fruit_Pests', 'Pest: Mango Stone Weevil (Sternochetus mangiferae)
Category: Fruit_Pests
Host Plants: Mango (specific to mango seed/stone)
Damage: No external fruit damage visible; seed destroyed; premature fruit drop; larvae tunnel through cotyledons; affects seed viability for propagation
Identification: Adult: 7-9mm, brown-black mottled weevil; Larva: white, legless grub inside mango seed
Organic Control: Collect and destroy fallen infested fruits; tree hygiene — remove old bark; hot water seed treatment for nursery use (52°C for 15 min)
Chemical Control: Chlorpyrifos 20% EC (2ml/L) spray when adults are active (Feb-March); trunk banding with insecticide strips
Biological Control: No effective commercial biological control
IPM Notes: Major quarantine pest affecting mango export. Fumigation (Methyl Bromide or Phosphine) required for export. SIT being explored.', 'pests_db', 'Mango (specific to mango seed/stone)', 'Fruit_Pests,Sternochetus mangiferae', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (47, 'pest', 'White Grubs (Chafer Beetles) - Soil_Pests', 'Pest: White Grubs (Chafer Beetles) (Holotrichia consanguinea, Leucopholis lepidophora (multiple spp.))
Category: Soil_Pests
Host Plants: Sugarcane, Groundnut, Maize, Potato, Soybean, Turf grasses, Tree nurseries
Damage: Plants wilt suddenly (root destruction by grubs); patches of dead plants in field; soil becomes soft and easy to pull plants (roots eaten); adult beetles feed on tree leaves at night
Identification: Grubs: creamy white C-shaped, up to 30-50mm, brown head; Adults: brown to black beetles 15-35mm with lamellate antennae
Organic Control: Metarhizium anisopliae fungus (1×10⁹ spores/ml) soil application; ploughing to expose and destroy grubs; light traps for adults; neem cake 250 kg/ha
Chemical Control: Chlorpyrifos 20% EC (5L/ha) soil incorporation before planting; Carbofuran 3G (25 kg/ha); Phorate 10G; Imidacloprid seed treatment
Biological Control: Metarhizium anisopliae, Beauveria bassiana soil inoculants; Heterorhabditis bacteriophora (entomopathogenic nematode)
IPM Notes: Ploughing before monsoon onset exposes grubs to heat and predators; synchronize light trap monitoring with adult emergence; grub management is season-long', 'pests_db', 'Sugarcane, Groundnut, Maize, Potato, Soybean, Turf grasses, Tree nurseries', 'Soil_Pests,Holotrichia consanguinea, Leucopholis lepidophora (multiple spp.)', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (48, 'pest', 'Root Knot Nematode - Soil_Pests', 'Pest: Root Knot Nematode (Meloidogyne incognita, M. javanica, M. arenaria, M. hapla)
Category: Soil_Pests
Host Plants: Over 2,000 plant species; especially vegetables, tobacco, cotton, legumes
Damage: Above ground: wilting, chlorosis, stunting resembling nutrient deficiency; Below ground: characteristic root galls (knots), reduced and brown root system, secondary root pathogens
Identification: Microscopic (0.5-1mm); females become sedentary, pear-shaped inside galls; second-stage juveniles (J2) infectious stage; galls visible on roots as swellings
Organic Control: Marigold (Tagetes spp.) intercropping; neem cake 250kg/ha soil application; Paecilomyces lilacinus inoculant; castor cake; mustard cake; crop rotation with cereals
Chemical Control: Carbofuran 3G (33 kg/ha), Phorate 10G, Ethoprophos 10G at planting; soil fumigation with Dazomet or Metam sodium (pre-plant)
Biological Control: Purpureocillium lilacinum (formerly Paecilomyces lilacinus), Pochonia chlamydosporia, Trichoderma harzianum, Bacillus firmus (VOTiVO), Steinernema carpocapsae
IPM Notes: Soil solarization (polyethylene film on moist soil for 6-8 weeks) highly effective; Mi-1.2 gene resistance in tomato; grafting onto resistant rootstocks effective in cucurbits', 'pests_db', 'Over 2,000 plant species; especially vegetables, tobacco, cotton, legumes', 'Soil_Pests,Meloidogyne incognita, M. javanica, M. arenaria, M. hapla', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (49, 'pest', 'Rice Weevil - Storage_Pests', 'Pest: Rice Weevil (Sitophilus oryzae)
Category: Storage_Pests
Host Plants: Rice, Wheat, Maize, Barley, Sorghum — stored grains
Damage: Grain kernels hollowed out; dust and frass in stored grain; characteristic exit holes; grain losses 20-40%; quality deterioration
Identification: Adult: 2.5-3.5mm, reddish-brown with 4 pale red-yellow spots on elytra; long snout (rostrum); Larvae: white, legless grub inside grain
Organic Control: Clean dry grain storage (< 14% moisture); diatomaceous earth 1.5g/kg mixed with grain; bay leaves in storage; neem leaf powder mixed with grain; hermetic storage (PICS bags, metal silos)
Chemical Control: Phosphine fumigation (Aluminium phosphide tablets 3 tablets/tonne); Pyrethrin spray on empty stores; Deltamethrin WP on wall surfaces; Pirimiphos-methyl admixture
Biological Control: No practical biological control for storage pests
IPM Notes: Clean storage is the most important preventive measure. Never store wet grain. Use hermetic bags (PICS/GrainPro) for smallholder storage. Monitor with traps regularly.', 'pests_db', 'Rice, Wheat, Maize, Barley, Sorghum — stored grains', 'Storage_Pests,Sitophilus oryzae', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (50, 'pest', 'Lesser Grain Borer - Storage_Pests', 'Pest: Lesser Grain Borer (Rhyzopertha dominica)
Category: Storage_Pests
Host Plants: Wheat, Rice, Maize, Barley, Sorghum — stored grains
Damage: Flour dust from feeding activity; grain kernels bored from outside; ''rice dust''; severe infestations cause 30-50% losses; heat generation from infested grain
Identification: Adult: 2.5-3mm, dark brown, elongated with head underneath pronotum; cylindrical shape; Larvae: white grub in grain or debris
Organic Control: Hermetic storage, diatomaceous earth, proper drying below 12% moisture
Chemical Control: Phosphine fumigation, Pirimiphos-methyl grain protectant
Biological Control: Limited; Theocolax elegans (ectoparasitoid wasp)
IPM Notes: More damaging than rice weevil because it attacks hard grain; thrives in lower moisture conditions', 'pests_db', 'Wheat, Rice, Maize, Barley, Sorghum — stored grains', 'Storage_Pests,Rhyzopertha dominica', NULL, '2026-06-26 15:47:47', '2026-06-26 15:47:47'),
    (51, 'nutrient', 'Carbon (C) - Plant Nutrition', 'Nutrient: Carbon (C)
Type: Non-mineral macronutrient
Functions: Primary component of all organic molecules, Photosynthesis (CO2 fixation), Structural component of plant body
Deficiency Name: 
Deficiency Signs: None (CO2 naturally available)
Affected Leaf Position: 
Toxicity: 
Fertilizer Sources: CO2 enrichment in greenhouses
Critical Crops: All crops', 'nutrients_db', 'All crops', 'nutrition,Carbon,C', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (52, 'nutrient', 'Hydrogen (H) - Plant Nutrition', 'Nutrient: Hydrogen (H)
Type: Non-mineral macronutrient
Functions: Component of all organic molecules, Water transport, pH regulation in cells
Deficiency Name: 
Deficiency Signs: Wilting, leaf roll
Affected Leaf Position: 
Toxicity: 
Fertilizer Sources: Irrigation water
Critical Crops: All crops', 'nutrients_db', 'All crops', 'nutrition,Hydrogen,H', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (53, 'nutrient', 'Oxygen (O) - Plant Nutrition', 'Nutrient: Oxygen (O)
Type: Non-mineral macronutrient
Functions: Aerobic respiration, Component of all organic molecules, Root aeration
Deficiency Name: 
Deficiency Signs: Yellow leaves, root browning, sulfide smell
Affected Leaf Position: 
Toxicity: 
Fertilizer Sources: Drainage improvement, Raised beds
Critical Crops: All crops, especially in waterlogged areas', 'nutrients_db', 'All crops', 'nutrition,Oxygen,O', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (54, 'nutrient', 'Nitrogen (N) - Plant Nutrition', 'Nutrient: Nitrogen (N)
Type: Primary Macronutrient
Functions: Component of amino acids, proteins, enzymes, Chlorophyll synthesis (green color), Nucleic acid component (DNA, RNA), Promotes vegetative growth, Enzyme activation
Deficiency Name: Nitrogen Deficiency (Chlorosis)
Deficiency Signs: Pale yellow-green color starting from older leaves (lower); progresses upward; stunted growth; thin spindly stems; early maturity
Affected Leaf Position: Older/Lower leaves first (N is mobile, remobilized to young leaves)
Toxicity: Dark green, lodging, delayed maturity, reduced grain quality, excessive vegetative growth, hollow stems
Fertilizer Sources: Urea (46% N) — most common, Ammonium Nitrate (34% N), Ammonium Sulphate (21% N, 24% S), Calcium Ammonium Nitrate (25% N), DAP (18% N, 46% P2O5), Legume green manure (biological fixation), FYM (0.5-1.5% N)
Critical Crops: Rice, Wheat, Maize, Vegetables, Cotton', 'nutrients_db', 'All crops', 'nutrition,Nitrogen,N', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (55, 'nutrient', 'Phosphorus (P) - Plant Nutrition', 'Nutrient: Phosphorus (P)
Type: Primary Macronutrient
Functions: Root development and growth, Energy transfer (ATP, ADP), Nucleic acid component (DNA, RNA), Cell membrane phospholipids, Early plant establishment and tillering, Seed and fruit development
Deficiency Name: Phosphorus Deficiency (Purpling)
Deficiency Signs: Dark green to purple/red color on older leaves and stems (anthocyanin accumulation); thin, weak roots; delayed maturity; small seeds
Affected Leaf Position: Older leaves first (P is mobile)
Toxicity: Zinc and iron deficiency symptoms (P-induced micronutrient deficiency); stunted growth when soil P very high
Fertilizer Sources: DAP — Diammonium Phosphate (46% P2O5, 18% N), SSP — Single Super Phosphate (16% P2O5, 11% S, 20% Ca), TSP — Triple Super Phosphate (46% P2O5), Rock Phosphate (28-35% P2O5) — slow release in acid soils, Ammonium Polyphosphate, Bone meal (20-25% P2O5)
Critical Crops: All crops; especially legumes, root crops, cereals', 'nutrients_db', 'All crops', 'nutrition,Phosphorus,P', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (56, 'nutrient', 'Potassium (K) - Plant Nutrition', 'Nutrient: Potassium (K)
Type: Primary Macronutrient
Functions: Stomatal regulation (drought resistance), Enzyme activation (>60 enzymes), Protein synthesis, Disease resistance and strong cell walls, Transport of sugars and nutrients in phloem, Quality improvement (sugar content, fruit firmness, starch)
Deficiency Name: Potassium Deficiency (Potash Starvation)
Deficiency Signs: Brown scorching and curling of leaf tips and margins (leaf scorch/marginal necrosis) starting on older leaves; brown spots inside leaf margin; weak stems; lodging in cereals
Affected Leaf Position: Older/Lower leaves first (K is mobile)
Toxicity: Calcium and magnesium deficiency symptoms (K antagonism); salt effects in sandy soils
Fertilizer Sources: Muriate of Potash / MOP (60% K2O) — most common, Sulphate of Potash / SOP (50% K2O, 18% S) — premium for Cl-sensitive crops, Potassium Nitrate (44% K2O, 13% N) — for fertigation, Potassium Chloride (KCl), Wood ash (5-10% K2O) — organic source
Critical Crops: Potato, Banana, Sugarcane, Tobacco, Cotton, Tomato', 'nutrients_db', 'All crops', 'nutrition,Potassium,K', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (57, 'nutrient', 'Calcium (Ca) - Plant Nutrition', 'Nutrient: Calcium (Ca)
Type: Secondary Macronutrient
Functions: Cell wall structure (calcium pectate in middle lamella), Cell membrane integrity, Signal transduction, Enzyme activation, Root tip and young leaf development
Deficiency Name: Calcium Deficiency
Deficiency Signs: Affects only new/young leaves and growing points (Ca is immobile); tip burn (leaf tips die), blossom end rot in tomato/pepper, bitter pit in apple, tip burn in lettuce and cabbage, hollow heart in brassica
Affected Leaf Position: Young/new leaves and growing points (Ca is IMMOBILE — not remobilized)
Toxicity: Rare; reduces Mg, K, Zn uptake at very high Ca
Fertilizer Sources: Agricultural Lime CaCO3 (36-40% Ca) — pH correction, Dolomitic Lime — CaMg(CO3)2 — provides Ca + Mg, Gypsum CaSO4 (23% Ca, 18% S) — for sodic soils; doesn''t raise pH, Calcium Nitrate (19% Ca, 15.5% N) — for fertigation, SSP (20% Ca, 16% P2O5)
Critical Crops: Tomato, Pepper, Apple, Celery, Lettuce, Brassicas', 'nutrients_db', 'All crops', 'nutrition,Calcium,Ca', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (58, 'nutrient', 'Magnesium (Mg) - Plant Nutrition', 'Nutrient: Magnesium (Mg)
Type: Secondary Macronutrient
Functions: Central atom of chlorophyll molecule, Enzyme activation (100+ enzymes), Phosphate transport within plant, Sugar and protein synthesis, Activates photosynthesis
Deficiency Name: Magnesium Deficiency (Interveinal Chlorosis)
Deficiency Signs: Interveinal chlorosis on older leaves — yellowing between the veins while veins remain green; often starts as pale green, then yellow, then reddish-purple margins; leaves may curl upward
Affected Leaf Position: Older/Lower leaves first (Mg is mobile)
Toxicity: Rare outdoors; possible in greenhouse soils; reduces Ca uptake at very high Mg
Fertilizer Sources: Kieserite — Magnesium Sulphate (16% Mg, 22% S), Magnesium Sulphate (Epsom Salt) — (10% Mg) for foliar spray, Dolomitic Lime — CaMg(CO3)2, Magnesia (MgO), Langbeinite (K2Mg2(SO4)3)
Critical Crops: Apple, Maize, Potato, Tomato, Grapes', 'nutrients_db', 'All crops', 'nutrition,Magnesium,Mg', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (59, 'nutrient', 'Sulfur (S) - Plant Nutrition', 'Nutrient: Sulfur (S)
Type: Secondary Macronutrient
Functions: Component of amino acids (cysteine, methionine), Protein synthesis, Enzyme cofactor, Glucosinolate synthesis (brassicas), Chlorophyll synthesis support, Flavor compounds in Alliums
Deficiency Name: Sulfur Deficiency
Deficiency Signs: Interveinal chlorosis of YOUNG/NEW leaves (unlike Mg which affects old leaves) — pale yellow-green color of new leaves while old leaves remain green; stunted growth
Affected Leaf Position: Young/New leaves first (S is relatively immobile)
Toxicity: Sulfur toxicity rare in soils; atmospheric SO2 damage shows as leaf spots and margin burn
Fertilizer Sources: Ammonium Sulphate (24% S, 21% N), SSP (11% S), Kieserite (22% S, 16% Mg), Sulphate of Potash (18% S, 50% K2O), Gypsum CaSO4 (18% S), Wettable Sulfur (90-98% S) — fungicide + nutrient, Elemental Sulfur (90-100% S) — acidifier, slow release
Critical Crops: Onion, Garlic, Mustard, Canola, Sunflower, Sugarcane', 'nutrients_db', 'All crops', 'nutrition,Sulfur,S', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (60, 'nutrient', 'Iron (Fe) - Plant Nutrition', 'Nutrient: Iron (Fe)
Type: Micronutrient
Functions: Chlorophyll synthesis (not structural), Electron carrier in photosynthesis and respiration, Enzyme cofactor (catalase, peroxidase), Nitrogen fixation in legumes, Nitrate reduction
Deficiency Name: Iron Chlorosis (Lime-induced Chlorosis)
Deficiency Signs: Interveinal chlorosis on YOUNG leaves — bright yellow leaves with dark green veins; in severe cases entire leaf turns yellow then white; known as ''lime-induced chlorosis'' on calcareous soils
Affected Leaf Position: Young/New leaves first (Fe is immobile)
Toxicity: In waterlogged rice soils: bronze-brown speckling of leaf surface starting from tips; ''bronzing''; roots become brown and rotten; Reduced tillering
Fertilizer Sources: FeSO4 (Iron Sulphate) — soil application 25-50 kg/ha, Fe-EDTA, Fe-DTPA, Fe-EDDHA — chelated iron (most effective, especially at high pH), Fe-EDDHA — most stable in high pH soils (most expensive), Foliar spray: FeSO4 0.5-1% (5-10g/L)
Critical Crops: Soybean, Groundnut, Citrus, Grapes, Sorghum (in calcareous soils)', 'nutrients_db', 'All crops', 'nutrition,Iron,Fe', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (61, 'nutrient', 'Zinc (Zn) - Plant Nutrition', 'Nutrient: Zinc (Zn)
Type: Micronutrient
Functions: Enzyme activation (300+ enzymes), Auxin synthesis (growth hormone), Protein synthesis, Chlorophyll formation, Carbohydrate metabolism, Pollen viability
Deficiency Name: Zinc Deficiency (Khaira Disease in Rice; Little Leaf in Fruits)
Deficiency Signs: In cereals: pale brown spots on mid-leaf, interveinal chlorosis; In fruits: small leaves (little leaf), shortened internodes (rosetting); In maize: broad white/yellow bands (white bud); Rice: ''khaira disease'' — pale orange-brown blotching of older leaves
Affected Leaf Position: Older to young leaves depending on crop
Toxicity: Root growth inhibition; interveinal chlorosis (Fe/Mn deficiency induced); common on contaminated soils
Fertilizer Sources: Zinc Sulphate Monohydrate (35% Zn) — most common; soil application 25 kg/ha, Zinc Sulphate Heptahydrate (21% Zn), Zinc Oxide (80% Zn) — slow release, Zinc Chelate (EDTA) — for fertigation, Foliar spray: ZnSO4 0.5% + lime 0.25%, Seed treatment: ZnSO4 solution soaking
Critical Crops: Rice (Khaira), Maize (white bud), Citrus, Apple, Cotton, Legumes', 'nutrients_db', 'All crops', 'nutrition,Zinc,Zn', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (62, 'nutrient', 'Manganese (Mn) - Plant Nutrition', 'Nutrient: Manganese (Mn)
Type: Micronutrient
Functions: Photosystem II water splitting (oxygen evolution), Enzyme activation (Mn-SOD), Nitrogen assimilation, Shikimate pathway (phenol synthesis)
Deficiency Name: Manganese Deficiency (Grey Speck in Oat; Pahala Blight in Sugarcane)
Deficiency Signs: Interveinal chlorosis of younger leaves; grey-green patches between veins; tissue may remain light green with distinct green veins; eventually necrosis; oat: ''grey speck''; cereals: stripe patterns; sugarcane: ''pahala blight''
Affected Leaf Position: Young/New leaves first (Mn is immobile)
Toxicity: Brown speckling of older leaves, irregular brown spots; marginal necrosis; symptoms of Fe and Ca deficiency (Mn-induced); common in acid soils
Fertilizer Sources: MnSO4 (32% Mn) — soil or foliar, Mn chelates — for high pH soils, Foliar spray: MnSO4 0.5% (5g/L)
Critical Crops: Oat, Sugar Beet, Soybean, Legumes, Fruit trees', 'nutrients_db', 'All crops', 'nutrition,Manganese,Mn', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (63, 'nutrient', 'Boron (B) - Plant Nutrition', 'Nutrient: Boron (B)
Type: Micronutrient
Functions: Cell wall structure (cross-links pectins), Reproduction (pollen tube growth, fertilization), Sugar translocation, Calcium utilization, Membrane integrity
Deficiency Name: Boron Deficiency (Hollow Heart, Heart Rot)
Deficiency Signs: Death of growing points (apical meristem); distorted, thick, brittle, curled young leaves; hollow heart in beet/turnip; sunflower head sterility; poor fruit set; corky/cracked fruits; hollow stem in brassica
Affected Leaf Position: Young leaves and growing points (B is immobile)
Toxicity: Marginal leaf burn of older leaves; yellow tips and margins; root damage; B has very narrow range between deficiency and toxicity
Fertilizer Sources: Borax Na2B4O7.10H2O (11% B) — soil application 0.5-1 kg/ha, Boric acid H3BO3 (17% B) — foliar spray 0.2-0.3%, Solubor (20% B) — soluble for spraying, Boron fertilizer granules — for mixed fertilizers
Critical Crops: Sunflower, Brassicas, Sugar Beet, Apple, Groundnut, Cotton', 'nutrients_db', 'All crops', 'nutrition,Boron,B', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (64, 'nutrient', 'Copper (Cu) - Plant Nutrition', 'Nutrient: Copper (Cu)
Type: Micronutrient
Functions: Photosynthesis (plastocyanin), Enzyme activation (polyphenol oxidase, ascorbate oxidase), Lignin synthesis (cell wall strength), Pollen tube growth
Deficiency Name: Copper Deficiency (Reclamation Disease)
Deficiency Signs: Wilting and dieback of growing tips (''die-back''); young leaves twisted, cup-shaped; pale blue-green color; in cereals: ''blind ear'' — twisted leaf sheaths preventing ear emergence; bluish-green hue
Affected Leaf Position: Young leaves and growing tips
Toxicity: Brown root discoloration; inhibited root growth; chlorosis; Fe deficiency symptoms
Fertilizer Sources: CuSO4 (25% Cu) — soil application 5-10 kg/ha, Cu chelates, Copper oxychloride (fungicide + nutrient), Foliar CuSO4 0.2% spray
Critical Crops: Wheat, Oat, Rye, Spinach, Onion, Fruit trees on organic soils', 'nutrients_db', 'All crops', 'nutrition,Copper,Cu', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (65, 'nutrient', 'Molybdenum (Mo) - Plant Nutrition', 'Nutrient: Molybdenum (Mo)
Type: Micronutrient
Functions: Nitrate reductase (NO3 to NH4 conversion), Nitrogen fixation in legumes (nitrogenase), Sulfite oxidase activity
Deficiency Name: Molybdenum Deficiency (Whiptail in Cauliflower)
Deficiency Signs: Interveinal chlorosis of older leaves; ''whiptail'' in cauliflower/broccoli — leaves fail to unfurl properly, look like a whip; marginal scorch; in legumes: poor nodulation and N fixation
Affected Leaf Position: Young leaves in brassica; older leaves in other crops
Toxicity: Very rare; excess Mo causes Cu deficiency; plants may appear Cu-deficient
Fertilizer Sources: Ammonium Molybdate (54% Mo) — tiny amounts needed 0.1-0.5 g/L foliar spray or seed treatment
Critical Crops: Cauliflower, Broccoli, Legumes (for N fixation), Maize', 'nutrients_db', 'All crops', 'nutrition,Molybdenum,Mo', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (66, 'nutrient', 'Chlorine (Cl) - Plant Nutrition', 'Nutrient: Chlorine (Cl)
Type: Micronutrient
Functions: Photosystem II water splitting, Stomatal regulation, Osmotic adjustment, Disease suppression
Deficiency Name: Chlorine Deficiency (Very Rare)
Deficiency Signs: Wilting; leaf bronzing; chlorosis; reduced growth — rarely seen in field crops as Cl is ubiquitous
Affected Leaf Position: Young leaves
Toxicity: Marginal leaf burn; bronze patches; premature leaf drop; salt stress symptoms
Fertilizer Sources: 
Critical Crops: Coconut (Cl responsive crop), Banana, Sugar Beet; Tobacco, Potato sensitive to Cl excess', 'nutrients_db', 'All crops', 'nutrition,Chlorine,Cl', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (67, 'nutrient', 'Nickel (Ni) - Plant Nutrition', 'Nutrient: Nickel (Ni)
Type: Micronutrient
Functions: Urease enzyme component (urea breakdown), Nitrogen metabolism, Seed germination and early vigor
Deficiency Name: Nickel Deficiency (Mouse Ear Disease in Pecan)
Deficiency Signs: Accumulation of urea in leaf tips (tissue damage); ''mouse ear'' in pecan (small stunted rounded leaflets); leaf tip necrosis; poor seed viability
Affected Leaf Position: 
Toxicity: Chlorosis; stunted growth; Fe deficiency induction; very toxic in acid soils
Fertilizer Sources: Nickel sulphate (very small amounts)
Critical Crops: Pecan, Wheat, Legumes', 'nutrients_db', 'All crops', 'nutrition,Nickel,Ni', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (68, 'nutrient', 'Cobalt (Co) - Plant Nutrition', 'Nutrient: Cobalt (Co)
Type: Beneficial Micronutrient (Legumes)
Functions: Component of vitamin B12 in Rhizobium bacteria, Essential for nitrogen fixation in legumes (indirect), Drought resistance
Deficiency Name: Cobalt Deficiency (affects legume N fixation)
Deficiency Signs: Legumes: poor nodulation and N fixation; symptoms mimic N deficiency; pale green plants; mostly on severely leached or coarse-textured soils
Affected Leaf Position: 
Toxicity: 
Fertilizer Sources: CoSO4 at 0.1-0.2 kg/ha very small dose
Critical Crops: Soybean, Clover, Alfalfa, Peanut (through Rhizobium)', 'nutrients_db', 'All crops', 'nutrition,Cobalt,Co', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (69, 'fertilizer_recommendation', 'Rice Fertilizer Recommendation', 'Crop: Rice
Fertilizer Recommendation:
General NPK: N120-P60-K60 kg/ha for irrigated; N60-P30-K30 for rainfed
N Application: Split: 50% basal + 25% active tillering + 25% panicle initiation
Special Notes: Urea use efficiency improved by LCC (Leaf Color Chart) monitoring; split N avoids luxury N and BLB risk
Critical Deficiencies: Zinc (Khaira), Iron toxicity in acid soils, Potassium in sandy soils', 'nutrients_db', 'Rice', 'fertilizer,Rice,nutrition', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (70, 'fertilizer_recommendation', 'Wheat Fertilizer Recommendation', 'Crop: Wheat
Fertilizer Recommendation:
General NPK: N120-P60-K40 kg/ha for HYV; N60-P30-K20 for local varieties
N Application: 50% basal + 25% CRI (crown root initiation) + 25% ear emergence
Special Notes: 
Critical Deficiencies: Zinc, Sulfur, Iron (in calcareous soils)', 'nutrients_db', 'Wheat', 'fertilizer,Wheat,nutrition', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (71, 'fertilizer_recommendation', 'Maize Fertilizer Recommendation', 'Crop: Maize
Fertilizer Recommendation:
General NPK: N180-P80-K60 kg/ha for high-yielding hybrids
N Application: 33% basal + 33% V6 (knee high) + 33% tasseling
Special Notes: 
Critical Deficiencies: Zinc (white bud), Nitrogen (main limiter)', 'nutrients_db', 'Maize', 'fertilizer,Maize,nutrition', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (72, 'fertilizer_recommendation', 'Tomato Fertilizer Recommendation', 'Crop: Tomato
Fertilizer Recommendation:
General NPK: N180-P120-K180 kg/ha typical for greenhouse/high-yield
N Application: Split through fertigation: 20% at transplanting, 30% vegetative, 30% fruiting, 20% late
Special Notes: EC of fertigation solution: 1.5-3.5 dS/m; balanced Ca:K ratio in fertigation crucial for quality
Critical Deficiencies: Calcium (BER), Magnesium, Potassium', 'nutrients_db', 'Tomato', 'fertilizer,Tomato,nutrition', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (73, 'fertilizer_recommendation', 'Potato Fertilizer Recommendation', 'Crop: Potato
Fertilizer Recommendation:
General NPK: N180-P100-K200 kg/ha — high K requirement for starch quality
N Application: 50% basal + 50% at hilling; avoid late N (reduces specific gravity)
Special Notes: Chloride (MOP) acceptable, but SOP preferred for better specific gravity and taste; use sulfate forms
Critical Deficiencies: Calcium, Magnesium, Boron', 'nutrients_db', 'Potato', 'fertilizer,Potato,nutrition', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (74, 'fertilizer_recommendation', 'Cotton Fertilizer Recommendation', 'Crop: Cotton
Fertilizer Recommendation:
General NPK: N150-P60-K60 kg/ha for irrigated; N100-P40-K40 for rainfed
N Application: 1/3 basal + 1/3 at first square + 1/3 at first flower
Special Notes: 
Critical Deficiencies: Potassium (fiber quality), Boron (boll setting), Zinc', 'nutrients_db', 'Cotton', 'fertilizer,Cotton,nutrition', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (75, 'fertilizer_recommendation', 'Sugarcane Fertilizer Recommendation', 'Crop: Sugarcane
Fertilizer Recommendation:
General NPK: N280-P120-K160 kg/ha planted crop; ratoon: N240-P80-K140
N Application: Split every 45-60 days; last application before 150 days
Special Notes: 
Critical Deficiencies: Zinc, Iron, Sulfur, Silicon', 'nutrients_db', 'Sugarcane', 'fertilizer,Sugarcane,nutrition', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (76, 'fertilizer_recommendation', 'Mango Fertilizer Recommendation', 'Crop: Mango
Fertilizer Recommendation:
General NPK: 
N Application: 
Special Notes: 
Critical Deficiencies: Zinc, Boron, Potassium', 'nutrients_db', 'Mango', 'fertilizer,Mango,nutrition', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (77, 'fertilizer_recommendation', 'Banana Fertilizer Recommendation', 'Crop: Banana
Fertilizer Recommendation:
General NPK: N200-P100-K300 g/plant/year (high K crops)
N Application: Monthly split applications: 50g N every 2 months from planting
Special Notes: 
Critical Deficiencies: Potassium (most critical), Magnesium, Zinc, Boron', 'nutrients_db', 'Banana', 'fertilizer,Banana,nutrition', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (78, 'cultivation', 'Rice Cultivation Guide', 'Crop: Rice (Oryza sativa)
Origin: Southeast Asia (China-India border region)
Climate: Tropical and subtropical — Temperature: 21-37°C (germination 18-40°C); Rainfall: 1000-2000mm annual; most during growing season
Soil: Heavy clay or clay-loam soils with good water retention; pH: 5.0-7.0 (optimal 6.0-6.5)
Seed Rate: Transplanted: 25-30 kg/ha; Direct seeded: 80-100 kg/ha; Spacing: 20×15 cm or 20×20 cm; 2-3 seedlings per hill
Irrigation: Continuous flooding (5-7cm standing water) in paddy field; Water Requirement: 1000-2000mm total
Fertilizer: N120-P60-K60 for irrigated HYV
Harvest: Reaping by sickle or combine harvester; Yield: 3-8 t/ha (irrigated HYV); 1-2 t/ha (rainfed) t/ha', 'cultivation_db', 'Rice', 'cultivation,Rice,Oryza sativa', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (79, 'cultivation', 'Wheat Cultivation Guide', 'Crop: Wheat (Triticum aestivum)
Origin: Fertile Crescent (Middle East)
Climate: Cool temperate to sub-tropical — Temperature: Germination 3-25°C; optimal growth 15-21°C; grain fill 20-25°C; Rainfall: 375-875mm (rabi / winter crop; relies on residual moisture and irrigation)
Soil: Well-drained fertile loam or clay-loam soils; pH: 6.0-7.5
Seed Rate: 100-125 kg/ha (timely sown); 125-150 kg/ha (late sown); Spacing: 22.5 cm row spacing (seed drill); broadcast is less preferred
Irrigation: Flood/furrow; drip/sprinkler for water efficiency; Water Requirement: 400-500mm total
Fertilizer: N120-P60-K40 for HYV; N150 with S15 for better protein
Harvest: Combine harvester or manual harvesting + threshing; Yield: 3-6 t/ha irrigated; 1.5-2.5 t/ha rainfed t/ha', 'cultivation_db', 'Wheat', 'cultivation,Wheat,Triticum aestivum', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (80, 'cultivation', 'Tomato Cultivation Guide', 'Crop: Tomato (Solanum lycopersicum)
Origin: South America (Peru-Ecuador region)
Climate: Warm sub-tropical to temperate — Temperature: Optimal 20-24°C day; 13-17°C night; no frost tolerance; Rainfall: 600-1500mm; avoid during fruiting; ideal with irrigation
Soil: Well-drained sandy loam to clay loam with good organic matter; pH: 6.0-7.0
Seed Rate: ; Spacing: 75×60cm for indeterminate; 75×45cm for determinate varieties
Irrigation: Drip irrigation preferred; avoid overhead (disease); furrow if drip unavailable; Water Requirement: 600-1200mm total
Fertilizer: N150-200, P75-100, K150-200
Harvest: ; Yield: 25-40 t/ha (open-pollinated); 60-100 t/ha (hybrids, drip, greenhouse) t/ha', 'cultivation_db', 'Tomato', 'cultivation,Tomato,Solanum lycopersicum', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (81, 'cultivation', 'Potato Cultivation Guide', 'Crop: Potato (Solanum tuberosum)
Origin: Andes Mountains, South America
Climate: Cool temperate — Temperature: 15-20°C for tuber initiation; growth 18-25°C; Rainfall: 500-700mm
Soil: Well-drained sandy loam or loam; deep friable soils; pH: 5.2-6.4 (avoids scab at lower pH)
Seed Rate: ; Spacing: 60-75 cm × 15-20 cm (rows × plants)
Irrigation: Furrow or drip irrigation; Water Requirement: 500-700mm
Fertilizer: N180-P100-K200 (high K for quality)
Harvest: Mechanical digger or manual fork; avoid damage; Yield: 20-40 t/ha t/ha', 'cultivation_db', 'Potato', 'cultivation,Potato,Solanum tuberosum', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (82, 'cultivation', 'Mango Cultivation Guide', 'Crop: Mango (Mangifera indica)
Origin: Northeast India, Bangladesh, Myanmar
Climate: Tropical and subtropical — Temperature: 24-30°C during vegetative growth; cool dry period needed for flowering; Rainfall: 750-2500mm; dry period during flowering and fruiting essential
Soil: Deep well-drained alluvial/loamy soils; pH: 5.5-7.5
Seed Rate: ; Spacing: 
Irrigation: Drip irrigation preferred for bearing orchards; Water Requirement: 
Fertilizer: 
Harvest: Hand-pick with harvesting poles; 2cm stalk retained to prevent sap burn; Yield:  t/ha', 'cultivation_db', 'Mango', 'cultivation,Mango,Mangifera indica', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (83, 'cultivation', 'Cotton Cultivation Guide', 'Crop: Cotton (Gossypium hirsutum)
Origin: Mesoamerica (Mexico-Central America region)
Climate: Warm tropical and subtropical — Temperature: 21-30°C; minimum 15°C for germination; Rainfall: 500-1500mm; distributed throughout growing season
Soil: Deep loamy or clay-loam ''black cotton soil'' (vertisol) preferred; pH: 5.5-7.0
Seed Rate: ; Spacing: 
Irrigation: Furrow or drip; Water Requirement: 
Fertilizer: N150-P60-K60 for irrigated hybrid Bt cotton
Harvest: Repeated hand-pickings (3-4 pickings as bolls open); mechanical picking in USA; Yield:  t/ha', 'cultivation_db', 'Cotton', 'cultivation,Cotton,Gossypium hirsutum', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (84, 'cultivation', 'Sugarcane Cultivation Guide', 'Crop: Sugarcane (Saccharum officinarum and hybrids)
Origin: New Guinea (Pacific Islands)
Climate: Tropical and subtropical — Temperature: 27-38°C growing season; 12-20°C for maturation and sucrose accumulation; Rainfall: 1500-2500mm; needs dry period for sucrose accumulation
Soil: Deep, well-drained alluvial or loamy soil; pH: 6.0-8.0
Seed Rate: ; Spacing: 
Irrigation: Drip irrigation most efficient; furrow also used; Water Requirement: 1500-2500mm total
Fertilizer: N280-P120-K160 planted crop; N240-P80-K140 ratoon
Harvest: Manual harvesting (topped and detrashed) or mechanical harvester; Yield: 70-100 t/ha cane; 8-11 t/ha sugar t/ha', 'cultivation_db', 'Sugarcane', 'cultivation,Sugarcane,Saccharum officinarum and hybrids', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (85, 'cultivation', 'Banana Cultivation Guide', 'Crop: Banana (Musa spp. (acuminata, balbisiana and hybrids))
Origin: Southeast Asia (Papua New Guinea region)
Climate: Humid tropical — Temperature: 26-30°C; growth stops below 15°C and above 38°C; Rainfall: 2000-2500mm; well distributed throughout year; critical to avoid dry spells
Soil: Deep, fertile, well-drained loam; pH: 5.5-7.0
Seed Rate: ; Spacing: 
Irrigation: Drip irrigation (most efficient); micro-sprinkler; Water Requirement: 2000-2500mm total
Fertilizer: 
Harvest: Whole bunch harvested at once by cutting bunch stalk; Yield: 40-60 t/ha (good management); 25-35 t/ha normal t/ha', 'cultivation_db', 'Banana', 'cultivation,Banana,Musa spp. (acuminata, balbisiana and hybrids)', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (86, 'cultivation', 'Soybean Cultivation Guide', 'Crop: Soybean (Glycine max)
Origin: Northern China
Climate: Warm temperate to tropical — Temperature: 20-30°C; frost-sensitive; Rainfall: 600-1000mm
Soil: Well-drained loam to clay loam; pH: 6.0-7.0
Seed Rate: 80-100 kg/ha; Spacing: 45×5cm or 30×5cm depending on fertility
Irrigation: ; Water Requirement: 500-700mm
Fertilizer: N20-P80-K40 (minimal N needed with good Rhizobium inoculation)
Harvest: Combine harvester or manual; Yield: 1.5-3.0 t/ha t/ha', 'cultivation_db', 'Soybean', 'cultivation,Soybean,Glycine max', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (87, 'cultivation', 'Chickpea Cultivation Guide', 'Crop: Chickpea (Cicer arietinum)
Origin: Turkey and Middle East
Climate: Cool dry conditions — Temperature: 15-25°C; tolerates light frost at vegetative stage; Rainfall: 400-1000mm; sensitive to excess moisture
Soil: Well-drained sandy loam to clay loam; pH: 6.0-9.0 (wide tolerance)
Seed Rate: 60-80 kg/ha (desi); 100-120 kg/ha (kabuli); Spacing: 
Irrigation: ; Water Requirement: 
Fertilizer: 
Harvest: Manual or combine; threshing by power thresher; Yield: 1.5-2.5 t/ha t/ha', 'cultivation_db', 'Chickpea', 'cultivation,Chickpea,Cicer arietinum', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13'),
    (88, 'cultivation', 'Coconut Cultivation Guide', 'Crop: Coconut (Cocos nucifera)
Origin: Pacific/Southeast Asia (disputed)
Climate: Humid tropical — Temperature: 27-32°C; minimum 15°C; no frost tolerance; Rainfall: 1500-2500mm; well-distributed
Soil: Sandy loam to loamy soils; alluvial soils; pH: 5.5-8.0
Seed Rate: ; Spacing: 
Irrigation: Drip, basin, or flood; Water Requirement: 
Fertilizer: 
Harvest: ; Yield:  t/ha', 'cultivation_db', 'Coconut', 'cultivation,Coconut,Cocos nucifera', NULL, '2026-06-26 15:48:13', '2026-06-26 15:48:13');

DROP TABLE IF EXISTS medicinal_knowledge CASCADE;
CREATE TABLE medicinal_knowledge (
    id INTEGER PRIMARY KEY NOT NULL,
    plant_name VARCHAR(200) NOT NULL,
    botanical_name VARCHAR(300) NULL,
    family_name VARCHAR(100) NULL,
    ayurvedic_name VARCHAR(200) NULL,
    ayurvedic_uses VARCHAR(255) NULL,
    unani_name VARCHAR(200) NULL,
    tcm_name VARCHAR(200) NULL,
    homeopathic_uses VARCHAR(255) NULL,
    active_compounds VARCHAR(255) NULL,
    pharmacological_actions VARCHAR(255) NULL,
    therapeutic_uses VARCHAR(255) NULL,
    contraindications VARCHAR(255) NULL,
    dosage_forms VARCHAR(255) NULL,
    plant_parts_used VARCHAR(300) NULL,
    created_at TIMESTAMP NULL
);

DROP TABLE IF EXISTS nutrition_facts CASCADE;
CREATE TABLE nutrition_facts (
    id INTEGER PRIMARY KEY NOT NULL,
    food_name VARCHAR(200) NOT NULL,
    botanical_name VARCHAR(300) NULL,
    serving_100g DOUBLE PRECISION NULL,
    energy_kcal DOUBLE PRECISION NULL,
    protein_g DOUBLE PRECISION NULL,
    fat_g DOUBLE PRECISION NULL,
    carbohydrate_g DOUBLE PRECISION NULL,
    fiber_g DOUBLE PRECISION NULL,
    sugar_g DOUBLE PRECISION NULL,
    vitamin_c_mg DOUBLE PRECISION NULL,
    vitamin_a_ug DOUBLE PRECISION NULL,
    vitamin_b1_mg DOUBLE PRECISION NULL,
    vitamin_b2_mg DOUBLE PRECISION NULL,
    vitamin_b3_mg DOUBLE PRECISION NULL,
    vitamin_b6_mg DOUBLE PRECISION NULL,
    vitamin_b12_ug DOUBLE PRECISION NULL,
    vitamin_d_ug DOUBLE PRECISION NULL,
    vitamin_e_mg DOUBLE PRECISION NULL,
    vitamin_k_ug DOUBLE PRECISION NULL,
    calcium_mg DOUBLE PRECISION NULL,
    iron_mg DOUBLE PRECISION NULL,
    magnesium_mg DOUBLE PRECISION NULL,
    phosphorus_mg DOUBLE PRECISION NULL,
    potassium_mg DOUBLE PRECISION NULL,
    sodium_mg DOUBLE PRECISION NULL,
    zinc_mg DOUBLE PRECISION NULL,
    antioxidants VARCHAR(255) NULL,
    phytonutrients VARCHAR(255) NULL,
    glycemic_index INTEGER NULL,
    data_source VARCHAR(100) NULL,
    created_at TIMESTAMP NULL
);

DROP TABLE IF EXISTS seed_data CASCADE;
CREATE TABLE seed_data (
    id INTEGER PRIMARY KEY NOT NULL,
    crop_name VARCHAR(200) NOT NULL,
    botanical_name VARCHAR(300) NULL,
    variety_name VARCHAR(200) NULL,
    seed_color VARCHAR(100) NULL,
    seed_shape VARCHAR(100) NULL,
    seed_weight_g_1000 DOUBLE PRECISION NULL,
    seed_rate_kg_ha DOUBLE PRECISION NULL,
    germination_pct DOUBLE PRECISION NULL,
    germination_temp_C VARCHAR(50) NULL,
    seed_treatment_fungicide VARCHAR(200) NULL,
    seed_treatment_bioagent VARCHAR(200) NULL,
    seed_treatment_insecticide VARCHAR(200) NULL,
    pelleting BOOLEAN NULL,
    storage_temp_C VARCHAR(50) NULL,
    storage_humidity_pct VARCHAR(50) NULL,
    seed_viability_years INTEGER NULL,
    breeder_institute VARCHAR(200) NULL,
    release_year INTEGER NULL,
    dte_days INTEGER NULL,
    created_at TIMESTAMP NULL
);

COMMIT;
