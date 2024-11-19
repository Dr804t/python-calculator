  def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

    def test_modulo_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.modulo(10, 0)