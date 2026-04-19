const API_URL = "http://localhost:8000";

export const login = async (email, password) => {
  const res = await fetch(`${API_URL}/auth/login`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ email, password })
  });

  return res.json();
};

export const getRemittances = async (token) => {
  const res = await fetch(`${API_URL}/remittances/`, {
    headers: {
      Authorization: `Bearer ${token}`
    }
  });

  return res.json();
};

export const createRemittance = async (token, data) => {
  const res = await fetch(`${API_URL}/remittances/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`
    },
    body: JSON.stringify(data)
  });

  return res.json();
};

export const deleteRemittance = async (token, id) => {
  await fetch(`${API_URL}/remittances/${id}`, {
    method: "DELETE",
    headers: {
      Authorization: `Bearer ${token}`
    }
  });
};