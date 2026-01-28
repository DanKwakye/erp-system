import { useState } from 'react';
import Products from './pages/Products';
import Suppliers from './pages/Suppliers';
import Customers from './pages/Customers';
import Orders from './pages/Orders';
import Inventory from './pages/Inventory';

function App() {
  const [currentPage, setCurrentPage] = useState('products');

  const renderPage = () => {
    switch(currentPage) {
      case 'products': return <Products />;
      case 'suppliers': return <Suppliers />;
      case 'customers': return <Customers />;
      case 'orders': return <Orders />;
      case 'inventory': return <Inventory />;
      default: return <Products />;
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Header */}
      <header className="bg-white shadow">
        <div className="container mx-auto px-4 py-6">
          <h1 className="text-2xl font-bold text-gray-900">
             Terra Foods EMS
          </h1>
        </div>
      </header>

      {/* Navigation */}
      <nav className="bg-white border-b border-gray-200">
        <div className="container mx-auto px-4">
          <div className="flex space-x-8">
            <button
              onClick={() => setCurrentPage('products')}
              className={`py-4 px-2 border-b-2 font-medium text-sm ${
                currentPage === 'products'
                  ? 'border-green-600 text-green-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
              }`}
            >
              Products
            </button>
            <button
              onClick={() => setCurrentPage('suppliers')}
              className={`py-4 px-2 border-b-2 font-medium text-sm ${
                currentPage === 'suppliers'
                  ? 'border-green-600 text-green-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
              }`}
            >
              Suppliers
            </button>
            <button
              onClick={() => setCurrentPage('customers')}
              className={`py-4 px-2 border-b-2 font-medium text-sm ${
                currentPage === 'customers'
                  ? 'border-green-600 text-green-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
              }`}
            >
              Customers
            </button>
            <button
              onClick={() => setCurrentPage('orders')}
              className={`py-4 px-2 border-b-2 font-medium text-sm ${
                currentPage === 'orders'
                  ? 'border-green-600 text-green-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
              }`}
            >
              Orders
            </button>
            <button
              onClick={() => setCurrentPage('inventory')}
              className={`py-4 px-2 border-b-2 font-medium text-sm ${
                currentPage === 'inventory'
                  ? 'border-green-600 text-green-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
              }`}
            >
              Inventory
            </button>
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <main>
        {renderPage()}
      </main>
    </div>
  );
}

export default App;