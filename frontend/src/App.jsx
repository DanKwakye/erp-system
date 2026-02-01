import { useState } from 'react';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard';
import Products from './pages/Products';
import Suppliers from './pages/Suppliers';
import Customers from './pages/Customers';
import Orders from './pages/Orders';
import Inventory from './pages/Inventory';

function App() {
  const [currentPage, setCurrentPage] = useState('dashboard');

  const renderPage = () => {
    switch(currentPage) {
      case 'dashboard': return <Dashboard />;
      case 'products': return <Products />;
      case 'suppliers': return <Suppliers />;
      case 'customers': return <Customers />;
      case 'orders': return <Orders />;
      case 'inventory': return <Inventory />;
      default: return <Dashboard />;
    }
  };

  return (
    <div className="flex h-screen bg-gray-50">
      {/* Sidebar */}
      <Sidebar currentPage={currentPage} onNavigate={setCurrentPage} />
      
      {/* Main Content */}
      <div className="flex-1 overflow-auto">
        {renderPage()}
      </div>
    </div>
  );
}

export default App;