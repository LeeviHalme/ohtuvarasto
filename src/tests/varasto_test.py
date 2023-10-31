import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisaa_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(-8)

        # varastossa pitäisi olla tilaa saman verran kuin aikaisemminkin (10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)
    
    def test_lisaa_ylitayteen(self):
        self.varasto.lisaa_varastoon(100)

        # varastossa pitäisi olla vain niin monta tavaraa, kuin tilavuus on
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ota_negatiivinen_maara(self):
        maara = self.varasto.ota_varastosta(-10)

        # varastossa pitäisi olla tilaa saman verran kuin aikaisemminkin (10)
        self.assertAlmostEqual(maara, 0)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_ota_enemman_kuin_saldo(self):
        self.varasto.lisaa_varastoon(50)
        maara = self.varasto.ota_varastosta(100)

        # varastossa pitäisi olla tilaa ja määrä pitäisi olla 10 (koko tilavuus)
        self.assertAlmostEqual(maara, 10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_tulostus(self):
        self.assertAlmostEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")

    def test_negatiivinen_tilavuus(self):
        varasto = Varasto(-10, 5)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_negatiivinen_saldo(self):
        varasto = Varasto(10, -5)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_alkusaldo_yli_tilavuuden(self):
        varasto = Varasto(10, 50)
        self.assertAlmostEqual(varasto.saldo, 10)
