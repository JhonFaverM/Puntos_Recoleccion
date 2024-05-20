from fastapi import APIRouter, HTTPException
from src.models.puntosRec_model import PuntosRecoleccionModel
from src.services.puntosRec_service import PuntosRecoleccionService



servicio = PuntosRecoleccionService()
router = APIRouter(prefix="/Puntos_Recoleccion")

@router.post("/")
def create_punto_recoleccion(puntos_recoleccion: PuntosRecoleccionModel):
    try:
        if PuntosRecoleccionService.existe_id_reporte_ser("Puntos_Recoleccion", puntos_recoleccion.prueba):
            raise HTTPException(status_code=400, detail="Ya existe un punto con ese ID...")
        if not all([puntos_recoleccion.prueba]):
            raise HTTPException(status_code=400, detail="Todos los campos son requeridos para crear el punto.")
        if PuntosRecoleccionService.registrar_punto(puntos_recoleccion):
            return {"Mensaje": "Registro exitoso!!"}, 201
        else:
            raise HTTPException(status=500, detail="Error al registrar el punto.")
    except ValueError:
         raise HTTPException(status_code=400, detail="Formato de fecha incorrecto")
    