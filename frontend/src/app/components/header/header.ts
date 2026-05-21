import { Component, inject } from '@angular/core';
import { Auth } from '../../services/auth';

@Component({
  selector: 'app-header',
  imports: [],
  templateUrl: './header.html',
  styleUrl: './header.css',
})
export class Header {
  private auth = inject(Auth);

  isMenuOpen = false

  toggleMenu() {
    this.isMenuOpen = !this.isMenuOpen
  }

  logout() {
    this.auth.logout();
  }
}
