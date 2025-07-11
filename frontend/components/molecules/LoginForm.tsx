import { Ionicons } from '@expo/vector-icons';
import { useState } from 'react';
import { Text, View } from 'react-native';
import Button from '../atoms/Button';
import Input from '../atoms/Input';

export default function LoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    console.log('Iniciar sesión con:', email, password);
  };

  return (
    <View className="space-y-6 w-full mt-3">
      <Text className="text-xl text-white text-center mb-4 font-poppinsBold ">Inicia Sesión</Text>

      <View className="space-y-4">
        <Input
          placeholder="Correo electrónico"
          keyboardType="email-address"
          value={email}
          onChangeText={setEmail}
        />

      </View>

      <View className="space-y-4 py-6">

        <Input
          placeholder="Contraseña"
          secureTextEntry
          value={password}
          onChangeText={setPassword}
        />
      </View>

      <Button onPress={handleLogin} className="bg-green-600 flex-row justify-center items-center space-x-4 ">
        <>
          <Ionicons name="log-in-outline" size={20} color="white" />
          <Text className="text-white text-base font-poppins">Ingresar</Text>
        </>
      </Button>
    </View>
  );
}
