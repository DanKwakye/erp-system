import { useState } from 'react';
import Products from './pages/Products';
import Suppliers from './pages/Suppliers';

function App() {
  const [currentPage, setCurrentPage] = useState('products');

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
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <main>
        {currentPage === 'products' && <Products />}
        {currentPage === 'suppliers' && <Suppliers />}
      </main>
    </div>
  );
}

export default App;