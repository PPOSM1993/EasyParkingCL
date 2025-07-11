import { TextInput, TextInputProps } from 'react-native';

export default function Input(props: TextInputProps) {
  return (
    <TextInput
      className="w-full px-4 py-3 border border-gray-300 rounded-lg text-base text-gray-800 bg-white focus:border-blue-500 font-poppins"
      placeholderTextColor="#9CA3AF"
      {...props}
    />
  );
}
