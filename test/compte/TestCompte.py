"""
Test pour les comptes
"""

import unittest
from compte import Compte

class TestCompte(unittest.TestCase):
    def test_creation_compte_sans_param(self):
        compte =Compte()
        self.assertEqual(compte.solde,0.0)

    def test_creation_compte_avec_solde(self):
        compte=Compte(20.0)
        self.assertEqual(compte.solde, 20.0)

    def test_creation_compte_avec_solde_negatif(self):
        self.assertRaise(NegatifAtCreateError,
                         Compte,
                         -10.0)
        
    def test_crediter_compte_avec_positif(self):
        compte=Compte()
        compte.crediter(20.0)
        self.assertEqual(compte.solde,20.0)

    def test_crediter_compte_multiple(self):
        compte=Compte()
        compte.crediter(20.0)
        compte.crediter(5.0)
        self.assertEqual(compte.solde,25.0)

    def test_crediter_compte_avec_negatif(self):
        compte=Compte()
        self.assertRaises(NegatifCreditError,
                         compte.crediter,
                         -10.0)

    def test_debiter_compte_avec_positif(self):
        compte=Compte(40.0)
        compte.debiter(20.0)
        self.assertEqual(compte.solde,20.0)

    def test_debiter_compte_multiple(self):
        compte=Compte(25.0)
        compte.debiter(20.0)
        compte.debiter(5.0)
        self.assertEqual(compte.solde,0.0)

    def test_debiter_compte_en_negatif(self):
        compte=Compte()
        self.assertRaises(NegatifCreditError,
                          compte.debiter,
                          10.0)

    def test_debiter_compte_avec_negatif(self):
        compte=Compte(40.0)
        self.assertRaises(NegatifCreditError,
                         compte.debiter,
                         -10.0)

if __name__ == '__main__':
    unittest.main()
