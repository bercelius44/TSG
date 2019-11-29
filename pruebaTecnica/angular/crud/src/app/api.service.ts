import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  get_responsables = 'http://localhost:8444/get-responsables/';
  get_responsable = 'http://localhost:8444/get-responsable=';
  create_responsable = 'http://localhost:8444/create-responsable/';
  update_responsables = 'http://localhost:8444/update-responsable=';
  delete_responsables = 'http://localhost:8444/delete-responsable=';

  get_resources = 'http://localhost:8444/get-resources/';
  get_resource_serial = 'http://localhost:8444/get-resource-serial=';
  get_resource_tipo = 'http://localhost:8444/get-resource-tipo=';
  get_resource_marca = 'http://localhost:8444/get-resource-marca=';
  create_resource = 'http://localhost:8444/create-resource/';
  update_resource = 'http://localhost:8444/update-resource=';
  delete_resource = 'http://localhost:8444/delete-resource=';

  httpHeaders = new HttpHeaders({'Content-Type': 'application/json'});

  constructor(private http: HttpClient) { }

  getAllResponsables(): Observable<any>{
    return this.http.get(this.get_responsables, {headers: this.httpHeaders});
  }

  getOnResponsable(id): Observable<any>{
    return this.http.get(this.get_responsable + id + '/', {headers: this.httpHeaders});
  }

  updateResponsable(responsable): Observable<any>{
    const body = {id: responsable.id, nombre: responsable.nombre, telefono: responsable.telefono, tipo: responsable.tipo}
    return this.http.put(this.update_responsables + responsable.id + '/', body, {headers: this.httpHeaders});
  }

  createResponsable(responsable): Observable<any>{
    const body = {id: responsable.id, nombre: responsable.nombre, telefono: responsable.telefono, tipo: responsable.tipo}
    return this.http.post(this.create_responsable, body, {headers: this.httpHeaders});
  }

  deleteResponsable(id): Observable<any>{
    return this.http.delete(this.delete_resource + id + '/', {headers: this.httpHeaders});
  }

  createResource(resource): Observable<any>{
    const body = {serial: resource.serial, 
                  id_encargado: resource.id_encargado, 
                  marca: resource.marca, 
                  tipo: resource.tipo, 
                  proveedor: resource.proveedor, 
                  valor_comercial: resource.valor_comercial, 
                  fecha_compra: resource.fecha_compra, 
                  estado: resource.estado, 
                  fecha_asignacion: resource.fecha_asignacion}

    return this.http.post(this.create_resource, body, {headers: this.httpHeaders});
  }

}
