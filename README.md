
# Coffee Shop Domain Model

This project models a Coffee Shop using Python classes to represent key entities: `Customer`, `Coffee`, and `Order`. It simulates a simple ordering system where customers can place orders for different types of coffee, and we can track various relationships and statistics such as the number of orders, customers' favorite coffee, and average prices.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Creating Customers](#creating-customers)
  - [Creating Coffees](#creating-coffees)
  - [Placing Orders](#placing-orders)
  - [Getting Customer Orders](#getting-customer-orders)
  - [Coffee Statistics](#coffee-statistics)
  - [Finding the Most Aficionado](#finding-the-most-aficionado)
- [Running Tests](#running-tests)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Coffee Shop project models three main entities:
- **Customer**: Represents a coffee shop customer.
- **Coffee**: Represents different types of coffee.
- **Order**: Represents an order placed by a customer for a specific coffee, including the price.

### Relationships:
- A `Customer` can place multiple orders.
- A `Coffee` can be ordered many times by different customers.
- Each `Order` belongs to one `Customer` and one `Coffee`.
- There is a many-to-many relationship between `Customer` and `Coffee` through `Order`.

## Features

- **Customer management**: Create customers and track their coffee orders.
- **Coffee management**: Track the number of times a coffee has been ordered and calculate its average price.
- **Order management**: Place orders with associated customers and coffees.
- **Statistics**: Find which customer has spent the most money on a particular coffee.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/coffee-shop.git
   cd coffee-shop
