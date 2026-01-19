import Products from './pages/Products';

function App() {
  return (
    <div className='min-h-screen bg-gray-100'>
      {/* Header */}
      <header className='big-white shadow'>
        <div className='container mx-auto px-4 py-6'>
          <h1 className='text-2xl font-bold text-gray-900'>
            Terra Foods EMS
          </h1>
        </div>
      </header>

      {/* Main Content */}
      <main>
        <Products />
      </main>
    </div>
  );
}


export default App;