from fastapi import APIRouter, HTTPException
from src.models.puntosRec_model import PuntosRecoleccionModel
from src.services.puntosRec_service import PuntosRecoleccionService



servicio = PuntosRecoleccionService()
router = APIRouter(prefix="/Puntos_Recoleccion")

@router.post("/")
def create_punto_recoleccion(puntos_recoleccion: PuntosRecoleccionModel):
    try:
        if PuntosRecoleccionService.existe_id_punto_ser("Puntos_Recoleccion", puntos_recoleccion.id):
            raise HTTPException(status_code=400, detail="Ya existe un punto con ese ID...")
        if not all([puntos_recoleccion.id, puntos_recoleccion.point_status, puntos_recoleccion.neighborhood, puntos_recoleccion.coordinates]):
            raise HTTPException(status_code=400, detail="Todos los campos son requeridos para crear el punto.")
        if PuntosRecoleccionService.registrar_punto(puntos_recoleccion):
            return {"Mensaje": "Registro exitoso!!"}, 201
    except ValueError:
         raise HTTPException(status_code=400, detail="Formato de fecha incorrecto")
     
     
@router.get("/")
def obtener_todos_puntos():
    try:
        return servicio.obtener_todos_puntos()
    except HTTPException as e:
        raise HTTPException(status_code=400, detail=f"Error al obtener los puntos de ubicación: {e}")
    
    
@router.get("/buscar_por_id")
def buscar_punto_por_id(id: str):
    try:
        return servicio.buscar_punto_por_id(id)#Ruta trae del servicio
    except HTTPException as e:
        raise HTTPException(status_code=400, detail=f"Error al obtener los reportes por id: {e}")
    
    
@router.put("/actualizar_por_id")
def actualizar_punto_por_id(id: str, puntos_recoleccion: PuntosRecoleccionModel):
        if id != puntos_recoleccion.id:
            raise HTTPException(status_code=400, detail="No se permite modificar el ID del punto.")
        if not PuntosRecoleccionService.existe_id_punto_ser("Puntos_Recoleccion", id):
            raise HTTPException(status_code=400, detail="No existe un punto de recolección con ese ID...")
        if not all([puntos_recoleccion.point_status, puntos_recoleccion.neighborhood, puntos_recoleccion.coordinates]):
            raise HTTPException(status_code=400, detail="Todos los campos son requeridos para actualizar el punto.")
        try:
            if PuntosRecoleccionService.actualizar_punto_por_id(id, puntos_recoleccion):
                return {"Mensaje": "Actualización exitosa"}, 200
        except HTTPException as e:
            raise HTTPException(status_code=400, detail=f"Error al intentar actualizar el punto por id: {e}")
        
    
@router.delete("/eliminar_punto_por_id")
def eliminar_punto_por_id(id: str):
    try:
        if not PuntosRecoleccionService.existe_id_punto_ser("Puntos_Recoleccion", id):
            raise HTTPException(status_code=400, detail="Reporte a eliminar no existe..")
        else:
            return servicio.eliminar_punto_por_id(id)#Ruta trae del servicio
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al eliminar el reporte por id: {e}")
    