import clsx from 'clsx';
import { ReactNode } from 'react';
import { TouchableOpacity, TouchableOpacityProps } from 'react-native';

type ButtonProps = TouchableOpacityProps & {
  children: ReactNode;
  className?: string;
};

export default function Button({ children, className, ...props }: ButtonProps) {
  return (
    <TouchableOpacity
      className={clsx("w-full py-3 rounded-lg items-center", className)}
      {...props}
    >
      {children}
    </TouchableOpacity>
  );
}
