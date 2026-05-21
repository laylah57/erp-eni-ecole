import { CanActivateFn, Router } from '@angular/router';
import { inject } from '@angular/core';
import { Auth } from '../services/auth';


export const authGuard: CanActivateFn = () => {
  const authService = inject(Auth)
  const router = inject(Router)

  if(!authService.isLoggedIn()){ // If no access token exists, it means the user is not logged in
    return router.createUrlTree(["/login"])
  }

  return true;
};
