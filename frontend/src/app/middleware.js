import agent from '../agent';
import {
  login,
  logout,
  register,
  updateUser,
} from '../features/auth/authSlice';

const localStorageMiddleware = (store) => (next) => (action) => {
  switch (action.type) {
    case register.fulfilled.type:
    case login.fulfilled.type:
      window.localStorage.setItem('jwt', action.payload.token);
      agent.setToken(action.payload.token);
      break;

    case logout.type:
      window.localStorage.removeItem('jwt');
      agent.setToken(undefined);
      break;

    case updateUser.fulfilled.type:
      window.localStorage.setItem('jwt', action.payload.token);
      agent.setToken(action.payload.token);
      break;
  }

  return next(action);
};

export { localStorageMiddleware };
