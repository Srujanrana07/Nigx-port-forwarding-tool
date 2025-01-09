# Nigx: Port-Forwarding-Tool

![Screenshot 2025-01-09 201459](https://github.com/user-attachments/assets/965e0f8b-b6c6-4ca4-acad-78a3c4aa5b03)

**Nigx - Port-Forwarding-Tool** is an open-source alternative to Ngrok, designed to provide seamless port forwarding and traffic redirection from a source port to a target address. This lightweight and efficient tool simplifies the process of exposing local services to the internet.

---

## Features

- **User-friendly CLI:** Intuitive command-line interface for easy setup.
- **Real-time logging:** Track connections and forwarded traffic.
- **Dynamic IP detection:** Automatically generates accessible links.
- **Multi-threaded:** Handles multiple connections efficiently.
- Supports TCP-based traffic forwarding.
- Ideal for developers testing webhooks, APIs, or services remotely.

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contributing](#contributing)
- [Contributor](#contributor)
- [How to Contribute](#how-to-contribute)


---

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/Srujanrana07/Nigx-port-forwarding-tool.git
   cd Tool
   ```
2. Run the Executable File:

   Double-click on the executable file to have the public serving link appear.

## Usage

1. Run the script:

   ```
   python port_forwarding.py
   ```
2. Enter the source port you wish to forward.
3. The tool will display a forwarding link, such as:
   ```
   Your forwarding link is: http://<public-ip>:<source-port>
   ```
4. Forwarded traffic will be redirected to the default target:

- **Host**: 8.8.8.8 (Google's public DNS server)
- **Port**: 80

5. To stop forwarding, press `Ctrl+C`.


## License

This project is licensed under the Apache License 2.0. See the [LICENSE](https://github.com/Srujanrana07/Nigx-port-forwarding-tool/blob/main/LICENSE) file for details.

## contributing

If you're interested in contributing to the Nigx Port Forwarding Tool project, you can start by exploring the code and opening issues or pull requests. We welcome contributions from developers of all experience levels.

You can contribute to the [Nigx Port Forwarding Tool project here](https://github.com/Srujanrana07/Nigx-port-forwarding-tool).

![Contributor Badge](https://img.shields.io/github/contributors/Srujanrana07/Nigx-port-forwarding-tool?style=flat-square)

### Contributor

- **Srujan Rana**: Developed and maintained the Nigx Port Forwarding Tool. You can find more of my work at [GitHub](https://github.com/Srujanrana07).

## How to Contribute

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Open a pull request.

We welcome any contributions, including bug fixes, new features, and documentation improvements!
