# libreria de testing 
import unittest
from taximetro import Taximetro
import colorama 
import time

# colores 
colorama.init()
color_reset = '\033[0m'
color_red = '\033[31m'
color_green = '\033[32m'
color_yellow = '\033[33m'

# funcion para imprimir bonito
def animated_print(text):
    print()
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()
    #print()
    #for char in text:
    #    print(color_yellow + "Testing: " + color_reset, end='', flush=True)
    #    time.sleep(0.05)
    #    print(color_green + " OK " + color_reset, end='', flush=True)
    #    time.sleep(0.05)
    #    print()
    #    time.sleep(0.05)

def check_value(value):

    checks = " "
    value_testing = "Testing: "
    value_ok = "OK"
    value_ko = "KO"
    for char in value_testing:
        print(color_yellow + char + color_reset, end='', flush=True)
        time.sleep(0.02)
        
    if value is True:
        for char in value_ok:
            print(color_green + char + color_reset, end='', flush=True)
            time.sleep(0.02)
    else:
        for char in value_ko:
            print(color_green + char + color_reset, end='', flush=True)
            time.sleep(0.02)
    print()

# clase a ejectuar tipo testing
class TestTaximetro(unittest.TestCase):
    def setUp(self):
        # se instancia la clase
        self.taximetro = Taximetro()

    def test_iniciar(self):
        animated_print(color_red + "test_iniciar - check variables" + ' \u2714 ' + color_reset)
        
        # se captura el valor inicial y se comprueba que sea el correcto
        valueActive = self.taximetro.taximetroActivo
        valueMove = self.taximetro.cocheEnMovimiento
        valueTotal = self.taximetro.tarifaTotal
        valueFrenado = self.taximetro.yaSeAfrenado
        valuePrecio_mov = self.taximetro.precio_mov
        valuePrecio_det = self.taximetro.precio_det
        valuePrecio_act = self.taximetro.precioActual
        valueA = self.taximetro.a
        valueActualizarPrecio = self.taximetro.actualizar_precio

        # con los metodos de la libreria unittest checamos cada valor
        self.assertFalse(valueActive)
        check_value(True) if not valueActive else check_value(False)
        self.assertFalse(valueMove)
        check_value(True) if not valueMove else check_value(False)
        self.assertEqual(valueTotal, 0)
        check_value(True) if valueTotal == 0 else check_value(False)
        self.assertEqual(valueFrenado, 0)
        check_value(True) if valueFrenado == 0 else check_value(False)
        self.assertEqual(valuePrecio_mov, 0)
        check_value(True) if valuePrecio_mov == 0 else check_value(False)
        self.assertEqual(valuePrecio_det, 0)
        check_value(True) if valuePrecio_det == 0 else check_value(False)
        self.assertEqual(valuePrecio_act, 0)
        check_value(True) if valuePrecio_act == 0 else check_value(False)
        self.assertEqual(valueA, 0)
        check_value(True) if valueA == 0 else check_value(False)
        self.assertFalse(valueActualizarPrecio)
        check_value(True) if not valueActualizarPrecio else check_value(False)
    
    def test_iniciar_carrera(self):
        animated_print(color_green + "test metodo iniciar carrera - check function" + ' \u2714 ' + color_reset)
        
        # se captura el valor dentro de la funcion
        self.taximetro.iniciar()
        valueData = self.taximetro.data
        valuePrecios = self.taximetro.aplicarPrecios
        valueLogs = self.taximetro.logs
        valueTarifaTotal = self.taximetro.tarifaTotal
        valueTaximetroActivo = self.taximetro.taximetroActivo
        valueActualizarPrecio = self.taximetro.actualizar_precio
        
        # Comprobar los resultados y comportamiento esperado
        self.assertIsNotNone(valueData)
        check_value(True) if valueData is not None else check_value(False)
        self.assertIsNotNone(valuePrecios)
        check_value(True) if valuePrecios is not None else check_value(False)
        self.assertIsNotNone(valueLogs)
        check_value(True) if valueLogs is not None else check_value(False)
        self.assertEqual(valueTarifaTotal, 0)
        check_value(True) if valueTarifaTotal == 0 else check_value(False)
        self.assertTrue(valueTaximetroActivo)
        check_value(True) if valueTaximetroActivo else check_value(False)
        self.assertTrue(valueActualizarPrecio)
        check_value(True) if valueActualizarPrecio else check_value(False)


    def test_mover_coche(self):
        animated_print(color_yellow + "test metodo mover coche - check function" + ' \u2714 ' + color_reset)

        # se captura el valor dentro de la funcion    
        self.taximetro.moverCoche()
        valueTaximetroActivo = self.taximetro.taximetroActivo
        valuecocheEnMovimiento = self.taximetro.cocheEnMovimiento

        # se comprueban los resultados
        self.assertFalse(valueTaximetroActivo)
        check_value(True) if not valueTaximetroActivo else check_value(False)
        self.assertFalse(valuecocheEnMovimiento)
        check_value(True) if not valuecocheEnMovimiento else check_value(False)
        self.assertTrue(self.taximetro.precioActual == self.taximetro.precio_mov)
        check_value(True) if self.taximetro.precioActual == self.taximetro.precio_mov else check_value(False)

                
    def test_detener_coche(self):
        animated_print(color_red + "test metodo detener coche - check function" + ' \u2714 ' + color_reset)

        # se captura el valor dentro de la funcion
        self.taximetro.detenerCoche()
        valueTaximetroActivo = self.taximetro.taximetroActivo
        valuecocheEnMovimiento = self.taximetro.cocheEnMovimiento
        valueYase = self.taximetro.yaSeAfrenado
        valuePrecio_det = self.taximetro.precio_det
        valuePrecio_mov = self.taximetro.precio_mov
        valueTarifaTotal = self.taximetro.tarifaTotal
        valueActualizarPrecio = self.taximetro.actualizar_precio
        valuePrecioActual = self.taximetro.precioActual
        valuePrecioDet = self.taximetro.precio_det


        # se comprueban los resultados 
        self.assertTrue(valuePrecioActual == valuePrecioDet)
        check_value(True) if valuePrecioActual == valuePrecioDet else check_value(False)
        self.assertFalse(valueTaximetroActivo)
        check_value(True) if not valueTaximetroActivo else check_value(False)
        self.assertFalse(valuecocheEnMovimiento)
        check_value(True) if not valuecocheEnMovimiento else check_value(False)
        self.assertFalse(valueYase)
        check_value(True) if not valueYase else check_value(False)
        self.assertTrue(valuePrecio_det == valuePrecio_mov)
        check_value(True) if valuePrecio_det == valuePrecio_mov else check_value(False)
        self.assertTrue(valueTarifaTotal == valuePrecio_det)
        check_value(True) if valueTarifaTotal == valuePrecio_det else check_value(False)
        self.assertFalse(valueActualizarPrecio)
        check_value(True) if not valueActualizarPrecio else check_value(False)


    def test_aplicar_precios(self):
        animated_print(color_green + "test metodo aplicar precios - check function" + ' \u2714 ' + color_reset)

        # se captura el valor dentro de la funcion
        self.taximetro.aplicarPrecios()
        valueprecios = self.taximetro.precios
        valueprecio1 = self.taximetro.precios[0]['precio_mov']
        valueprecio2 = self.taximetro.precios[0]['precio_det']
        valuePrecio_mov = self.taximetro.precio_mov
        valuePrecio_det = self.taximetro.precio_det
        valuePrecio_act = self.taximetro.precioActual
        valueActualizarPrecio = self.taximetro.actualizar_precio

        # se comprueban los resultados
        self.assertIsNotNone(valueprecios)
        check_value(True) if valueprecios is not None else check_value(False)
        self.assertTrue(valuePrecio_act == valuePrecio_det)
        self.assertFalse(valueActualizarPrecio)
        check_value(True) if not valueActualizarPrecio else check_value(False)
        self.assertTrue(valuePrecio_mov == valueprecio1)
        check_value(True) if valuePrecio_mov == valueprecio1 else check_value(False)
        self.assertTrue(valuePrecio_det == valueprecio2)
        check_value(True) if valuePrecio_det == valueprecio2 else check_value(False)


    def test_finalizarRecorrido(self):
        animated_print(color_yellow + "test metodo finalizar recorrido - check function" + ' \u2714 ' + color_reset)

        # se captura el valor dentro de la funcion
        self.taximetro.finalizarRecorrido()
        valuefcocheEnMovimiento = self.taximetro.cocheEnMovimiento
        valueTaximetroActivo = self.taximetro.taximetroActivo
        valuefDetenerPrecio = self.taximetro.precio_det

        # se comprueba los resultados
        self.assertFalse(valuefcocheEnMovimiento)
        check_value(True) if not valuefcocheEnMovimiento else check_value(False)
        self.assertFalse(valueTaximetroActivo)
        check_value(True) if not valueTaximetroActivo else check_value(False)
        self.assertTrue(valuefDetenerPrecio == 0)
        check_value(True) if valuefDetenerPrecio == 0 else check_value(False)


    def test_reinciar_valores(self):
        animated_print(color_red + "test metodo reiniciar valores - check function" + ' \u2714' + color_reset)

    
        # se captura el valor dentro de la funcion
        self.taximetro.reiniciarValores()
        valueTaximetroActivo = self.taximetro.taximetroActivo
        valuecocheEnMovimiento = self.taximetro.cocheEnMovimiento
        valueTarifaTotal = self.taximetro.tarifaTotal
        valuePrecio_mov = self.taximetro.precio_mov
        valuePrecio_det = self.taximetro.precio_det
        valuePrecio_act = self.taximetro.precioActual
        valueA = self.taximetro.a
        valueActualizarPrecio = self.taximetro.actualizar_precio

        # se comprueban que son correctos 
        self.assertFalse(valueTaximetroActivo)
        check_value(True) if not valueTaximetroActivo else check_value(False)
        self.assertFalse(valuecocheEnMovimiento)
        check_value(True) if not valuecocheEnMovimiento else check_value(False)
        self.assertEqual(valueTarifaTotal, 0)
        check_value(True) if valueTarifaTotal == 0 else check_value(False)
        self.assertEqual(valuePrecio_mov, 0)
        check_value(True) if valuePrecio_mov == 0 else check_value(False)
        self.assertEqual(valuePrecio_det, 0)
        check_value(True) if valuePrecio_det == 0 else check_value(False)
        self.assertEqual(valuePrecio_act, 0)
        check_value(True) if valuePrecio_act == 0 else check_value(False)
        self.assertEqual(valueA, 0)
        check_value(True) if valueA == 0 else check_value(False)
        self.assertFalse(valueActualizarPrecio)
        check_value(True) if not valueActualizarPrecio else check_value(False)

    
# primera llamada a la bb (el detalle al mostrar los test)
if __name__ == '__main__':
    try:
        animated_print(unittest.main(verbosity=0))
    except Exception as e:
        animated_print("Fallaron los test")
    print()
