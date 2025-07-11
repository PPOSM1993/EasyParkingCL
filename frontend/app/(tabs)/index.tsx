import { LinearGradient } from 'expo-linear-gradient';
import { View } from 'react-native';
import * as Animatable from 'react-native-animatable';
import LoginForm from '../../components/molecules/LoginForm';
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
          className="w-32 h-32 mb-2"
          resizeMode="contain"
        />

        <Animatable.View
          animation="fadeInUp"
          duration={1000}
          delay={200}
          className="space-y-6 px-4"
        >

        </Animatable.View>
        <LoginForm />

      </View>
    </LinearGradient>
  );
}
