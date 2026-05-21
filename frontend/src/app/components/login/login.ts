import { Component, inject } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';

import { Auth } from '../../services/auth';

@Component({
  selector: 'app-login',
  imports: [ReactiveFormsModule],
  templateUrl: './login.html',
  styleUrl: './login.css',
})
export class Login {
  private auth = inject(Auth);

  loginForm = new FormGroup({
    email: new FormControl("", [Validators.required, Validators.email]), // Decide what should be the minimum length
    // of the username
    password: new FormControl("", [Validators.required, Validators.minLength(6)]),
  });

  onSubmit() {
    if (this.loginForm.invalid) {
      this.loginForm.markAllAsTouched(); // Errors appear on all field if submit button clicked while invalid
      return;
    } else {
      const email = this.loginForm.controls.email.value ?? ''; // Value ?? empty string for type reasons.
      const password = this.loginForm.controls.password.value ?? '';

      this.auth.login(email, password).subscribe({
        next: (tokens) => {
          this.auth.saveTokens(tokens);
          this.auth.getCurrentUser().subscribe({
            next: (user) => console.log(user),
            error: (error) => console.error(error),
          });
        },
        error: (error) => console.error(error),
      });
    }
  }
}
