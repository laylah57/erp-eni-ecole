import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { Router } from '@angular/router';

interface AuthTokens {
  access: string;
  refresh: string;
}

interface CurrentUser {
  id: number;
  username: string;
  email: string;
  first_name: string | null;
  last_name: string | null;
  groups: string[];
}

@Injectable({
  providedIn: 'root',
})
export class Auth {
  private http = inject(HttpClient);
  private router = inject(Router)
  private apiUrl = 'http://127.0.0.1:8000/api';

  login(email: string, password: string) {
    return this.http.post<AuthTokens>(`${this.apiUrl}/token/`, {
      email,
      password,
    });
  }

  saveTokens(tokens: AuthTokens) {
    localStorage.setItem('access_token', tokens.access);
    localStorage.setItem('refresh_token', tokens.refresh);
  }

  getAccessToken() {
    return localStorage.getItem('access_token');
  }

  getRefreshToken() {
    return localStorage.getItem('refresh_token');
  }

  logout() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    this.router.navigate(['/login']);
  }

  getCurrentUser() {
    const accessToken = this.getAccessToken();
    if (!accessToken) {
      throw new Error('The access token does not exist');
    }
    return this.http.get<CurrentUser>(`${this.apiUrl}/accounts/me/`, {
      headers: {
        Authorization: `Bearer ${accessToken}`, // Eventually, use Angular HTTP interceptor
      },
    });
  }

  isLoggedIn() {
    return !!this.getAccessToken() // Same as this.getAcessToken() ? true : false
  }
}
