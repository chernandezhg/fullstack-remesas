import { useState, useEffect } from "react";
import { login, getRemittances, createRemittance, deleteRemittance } from "./api";
import "./App.css";

function App() {
  const [token, setToken] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [remittances, setRemittances] = useState([]);
  const [amount, setAmount] = useState("");
  const [receiver, setReceiver] = useState("");
  const [filter, setFilter] = useState("");

  // Cargar token guardado
  useEffect(() => {
    const savedToken = localStorage.getItem("token");
    if (savedToken) {
      setToken(savedToken);
    }
  }, []);

  // Cargar remesas automáticamente
  useEffect(() => {
    if (token) {
      loadRemittances();
    }
  }, [token]);

  // LOGIN
  const handleLogin = async () => {
    try {
      const data = await login(email, password);

      if (!data.access_token) {
        alert("Login falló");
        return;
      }

      setToken(data.access_token);
      localStorage.setItem("token", data.access_token);

      alert("Login exitoso");
    } catch (error) {
      console.error(error);
      alert("Error al conectar");
    }
  };

  // LOGOUT
  const handleLogout = () => {
    localStorage.removeItem("token");
    setToken("");
    setRemittances([]);
  };

  // GET
  const loadRemittances = async () => {
    try {
      const data = await getRemittances(token);
      setRemittances(data);
    } catch (error) {
      console.error(error);
    }
  };

  // CREATE
  const handleCreate = async () => {
    if (!amount || !receiver) {
      alert("Complete los campos");
      return;
    }

    await createRemittance(token, {
      amount: Number(amount),
      receiver_name: receiver
    });

    setAmount("");
    setReceiver("");

    loadRemittances();
  };

  // DELETE
  const handleDelete = async (id) => {
    await deleteRemittance(token, id);
    loadRemittances();
  };

  // FILTRO
  const filteredRemittances = remittances.filter(r =>
    r.receiver_name.toLowerCase().includes(filter.toLowerCase())
  );

  return (
    <div className="container">
      <h1>Remesas App</h1>

      {!token ? (
        <div className="card">
          <h2>Login</h2>
          <input placeholder="Email" onChange={e => setEmail(e.target.value)} />
          <input placeholder="Password" type="password" onChange={e => setPassword(e.target.value)} />
          <button onClick={handleLogin}>Login</button>
        </div>
      ) : (
        <>
          <button className="logout" onClick={handleLogout}>Logout</button>

          <div className="card">
            <h2>Crear remesa</h2>

            <input
              placeholder="Monto"
              type="number"
              value={amount}
              onChange={e => setAmount(e.target.value)}
            />

            <input
              placeholder="Destinatario"
              value={receiver}
              onChange={e => setReceiver(e.target.value)}
            />

            <button onClick={handleCreate}>Crear</button>
          </div>

          <div className="card">
            <h2>Lista de remesas</h2>

            <input
              placeholder="Buscar destinatario"
              onChange={e => setFilter(e.target.value)}
            />

            <ul>
              {filteredRemittances.map(r => (
                <li key={r.id}>
                  #{r.id} | {r.receiver_name} - ${r.amount} {r.currency} ({r.status})
                  <button onClick={() => handleDelete(r.id)}>❌</button>
                </li>
              ))}
            </ul>
          </div>
        </>
      )}
    </div>
  );
}

export default App;