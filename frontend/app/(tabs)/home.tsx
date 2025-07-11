import { Image, Text, View } from 'react-native';
import * as Animatable from 'react-native-animatable';
import Navbar from '../../components/organisms/Navbar';
import '../../styles/global.css';

export default function HomeScreen() {
  return (
    <View className="flex-1 bg-white">
      <Navbar />

      <View className="flex-1 justify-center items-center px-6 py-10">
        <Animatable.Image
          animation="fadeInDown"
          duration={1000}
          source={require('../../assets/images/logo.png')}
          className="w-32 h-32 mb-6"
          resizeMode="contain"
        />

        <Animatable.View
          animation="fadeInUp"
          duration={1000}
          delay={200}
          className="space-y-6 px-4"
        >


          <View className="space-y-6">

          <Text className="text-3xl font-extrabold text-blue-700 text-blue-600 text-center tracking-wide">
            Bienvenido a EasyParkingCL
          </Text>
          </View>

          <View className='space-y-6'>
          <Text className="text-md text-gray-700 text-justify leading-7 py-6">
            Conecta con estacionamientos inteligentes y accede a disponibilidad en tiempo real gracias a nuestra tecnología de inteligencia artificial.
          </Text>

          <Text className="text-base text-gray-500 text-center leading-relaxed italic">
            Usa el menú inferior para iniciar sesión o registrarte como nuevo usuario.
          </Text>
          </View>
        </Animatable.View>
      </View>
    </View>
  );
}
