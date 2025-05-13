import { createServer } from 'node:http';

// Hardcoded credentials for validation
const validUsername = 'admin';
const validPassword = 'password123';

// Create an HTTP server
const server = createServer((req, res) => {
  if (req.method === 'POST' && req.url === '/login') {
    let body = '';

    // Collect data from the request
    req.on('data', chunk => {
      body += chunk.toString();
    });

    req.on('end', () => {
      const { username, password } = JSON.parse(body);

      // Validate credentials
      if (username === validUsername && password === validPassword) {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ message: 'Login successful!' }));
      } else {
        res.writeHead(401, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ message: 'Invalid username or password.' }));
      }
    });
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Page Not Found');
  }
});

// Start the server on port 3000
server.listen(3000, '127.0.0.1', () => {
  console.log('Server is running on http://127.0.0.1:3000');
});