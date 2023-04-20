import logging as log
# EL % QUIERE DECIR QUE EL SISTEMA OP VA A MANDAR ARCHIVOS A ESTOS PARAMETROS
log.basicConfig(level=log.DEBUG, 
                format="%(asctime)s: %(levelname)s [%(filename)s] :%(lineno)s %(message)s ",
                datefmt= '%I:%M:%S %p',
                handlers=[log.FileHandler('capa_datos.log'),
                          log.StreamHandler()
                ])

if __name__=="_main_":
    log.debug("Mensaje debug")
    log.warning("Mensaje warning")
    log.error("Mensaje error")
    log.critical("Mensaje critico")