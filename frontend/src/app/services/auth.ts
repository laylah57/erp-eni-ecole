import { inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

interface Token {
  access: string;
  refresh: string
}

@Injectable({
  providedIn: 'root',
})
export class Auth {
  private http = inject(HttpClient)
  private apiUrl = 'http://127.0.0.1:8000/api'

  login(email: string, password: string) {
    return this.http.post<Token>(`${this.apiUrl}/token/`, {
      email,
      password
    })
  }
}
