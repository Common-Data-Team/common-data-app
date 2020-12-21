import {writable, get} from 'svelte/store'
import {setContext} from "svelte";

export const apiUrl = 'https://backend.commondata.ru/';
export const selfUrl = 'https://commondata.ru/';

export let user = writable("");


export async function sendForm(login, username, password, name) {
  let json_response = await fetch(
    apiUrl + (login ? 'users/token' : 'users/create?fio=' + name),
    {
      method: 'POST',
      credentials: 'omit',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: `username=${username}&password=${password}`
    },
  ).then(res => res.json());
  if (json_response.detail) {
    return login ? "Неправильная почта или пароль" : "Такая почта уже используется"
  }
  let {access_token, token_type, user_id} = json_response;
  setCookie('access_token', access_token, {samesite: 'lax'});
  setCookie('user_id', user_id, {samesite: 'lax'});
}


function setCookie(name, value, options = {}) {
  options = {
    path: '/',
    ...options
  };

  if (options.expires instanceof Date) {
    options.expires = options.expires.toUTCString();
  }

  let updatedCookie = encodeURIComponent(name) + "=" + encodeURIComponent(value);

  for (let optionKey in options) {
    updatedCookie += "; " + optionKey;
    let optionValue = options[optionKey];
    if (optionValue !== true) {
      updatedCookie += "=" + optionValue;
    }
  }

  document.cookie = updatedCookie;
}

export function getCookie(name) {
  let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

function deleteCookie(name) {
  setCookie(name, "", {
    'max-age': -1
  })
}


export function checkStoreAndCoockie() {
  if (get(user) === "") {
    let coockie_token = getCookie('access_token');
    if (coockie_token) {
      user.set(coockie_token)
    } else {
      return false;
    }
  }
  return true;
}


export async function authorizedRequest(apiPart, method, object) {
  if (!getCookie('access_token')) {
    return [null, "Unauthorized"]
  }
  let json_response = await fetch(apiUrl + apiPart, {
    method: method,
    headers: new Headers({
      'Accept': 'application/json',
      'Authorization': 'Bearer ' + getCookie('access_token'),
    }),
    body: JSON.stringify(object)
  }).then(res => res.json());
  if (json_response.detail && json_response.detail === "Not authenticated") {
    return [null, "Unauthorized"]
  } else if (json_response.detail) {
    return [null, json_response.detail]
  }
  return [json_response, null]
}

export function clearStoreAndCookie() {
  user = "";
  deleteCookie('access_token');
}

// API part
export const cache = new Map();
export let dataStore = writable({});
// TODO добавить контроль над сроком действия токена

export function getData(apiPart) {
  const store = writable(new Promise(() => {}));
  if (cache.has(apiPart)) {
    store.set(Promise.resolve(cache.get(apiPart)));
  }
  const load = async () => {
    const response = await fetch(apiUrl + apiPart);
    const data = await response.json();
    cache.set(apiPart, data);
    store.set(Promise.resolve(data));
    dataStore.set(data);
  };
  load();
  return store;
}
