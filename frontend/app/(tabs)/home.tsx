import { LinearGradient } from 'expo-linear-gradient';
import { Text, View } from 'react-native';
import * as Animatable from 'react-native-animatable';
import Navbar from '../../components/organisms/Navbar';
import '../../styles/global.css';

export default function HomeScreen() {
  return (
    <LinearGradient
      colors={['#0077B6', '#00B4D8']}
      className="flex-1"
    >
      <Navbar />

      <View className="flex-1 justify-center items-center px-6 py-10 space-y-6">
        <Animatable.Image
          animation="fadeInDown"
          duration={1000}
          source={require('../../assets/images/logo1.png')}
          className="w-40 h-32 mb-6"
          resizeMode="contain"
        />

        <Animatable.View
          animation="fadeInUp"
          duration={1000}
          delay={200}
          className="space-y-6 px-4"
        >
          <Text className="text-xl font-poppinsBold text-white text-center">
            Bienvenido a EasyParkingCL
          </Text>

          <Text className="text-sm text-white text-justify leading-relaxed py-6 font-poppins">
            App que te conecta con estacionamientos de manera inteligentes para acceder a disponibilidad en tiempo real con IA.
          </Text>

          <Text className="text-sm text-white text-center leading-relaxed font-poppins">
            Usa el menú inferior para iniciar sesión o registrarte como nuevo usuario.
          </Text>
        </Animatable.View>
      </View>
    </LinearGradient>
  );
}
