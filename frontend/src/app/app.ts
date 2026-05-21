import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApiService } from './services/api';

@Component({
selector: 'app-root',
standalone: true,
imports: [CommonModule],
templateUrl: './app.html',
})
export class AppComponent implements OnInit {

promotions: any[] = [];

constructor(private apiService: ApiService) {}

ngOnInit(): void {

console.log("COMPOSANT CHARGÉ");

this.apiService.getPromotions().subscribe({
next: (data: any) => {

console.log("DATA REÇUE =", data);

this.promotions = data;
},

error: (err: any) => {

console.error("ERREUR API =", err);
}
});
}
}
