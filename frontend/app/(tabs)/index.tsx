import { Text, View } from 'react-native';
import Button from '../../components/atoms/Button';
import Navbar from '../../components/organisms/Navbar';
import '../../styles/global.css';

export default function HomeScreen() {
  return (
    <View className="flex-1 bg-white">
      <Navbar />

      <View className="flex-1 justify-center items-center px-6 space-y-6">
        <Text className="text-3xl font-bold text-center text-blue-600">Bienvenido a EasyParkingCL</Text>
        <Text className="text-base text-gray-500 text-center">
          Encuentra y reserva estacionamientos inteligentes con IA y localización en tiempo real.
        </Text>

        <View className="w-full space-y-4 mt-6">
          <Button title="Iniciar sesión" onPress={() => alert('Login')} />
          <Button title="Crear cuenta" onPress={() => alert('Signup')} variant="secondary" />
        </View>
      </View>
    </View>
  );
}
