import { Component } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass'],
  providers: [ApiService]
})
export class AppComponent {
  title = 'Crud';
  responsables = [];
  resources = [];
  selectedResponsable;
  selectedResource;

  constructor(private api:ApiService){
    this.getResponsables();
    this.selectedResponsable = {id:-1, nombre:'', telefono:'', tipo:''}
    this.selectedResource = {serial: -1, id_encargado: -1, marca:'', tipo:'', proveedor:'', valor_comercial:'', fecha_compra:'', estado:'', fecha_asignacion:''}
  }

  getResponsables = () =>{    
    this.api.getAllResponsables().subscribe(
      data => {
        this.responsables = data;
        console.log(this.responsables)
      },
      error =>{
        console.log(error);
      }      
    )
  }

  responsableClicked = (responsable) => {
    this.api.getOnResponsable(responsable.id).subscribe(
      data => {
        this.selectedResponsable = data;
      },
      error =>{
        console.log(error);
      }      
    )
  }

  updateResponsable = () =>{
    this.api.updateResponsable(this.selectedResponsable).subscribe(
      data => {
        this.getResponsables();
      },
      error =>{
        console.log(error);
      }      
    )
  }

  createResponsable = () =>{
    this.api.createResponsable(this.selectedResponsable).subscribe(
      data => {
        this.responsables.push(data);        
      },
      error =>{        
        console.log(error.error);        
      }  
    )
  }

  deleteResponsable = () =>{
    this.api.deleteResponsable(this.selectedResponsable.id).subscribe(
      data => {
        this.getResponsables(); 
      },
      error =>{
        console.log(error);
      }      
    )
  }

  createResource = () =>{
    this.api.createResource(this.selectedResource).subscribe(
      data => {
        this.resources.push(data);        
      },
      error =>{        
        console.log(error.error);        
      }  
    )
  }
}